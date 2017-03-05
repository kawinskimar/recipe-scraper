import scrapy
import random
import urlparse
import socket
import datetime
from scrapy.http import Request
from allrecipes.items import AllrecipesItem
from scrapy.loader import ItemLoader as IL

class AllrecipesSpider(scrapy.Spider):
    name = 'allrecipes'
    allowed_domains = ['allrecipes.com']
    download_delay = 3

    start_urls = [
            # American recipe categories
            'http://allrecipes.com/recipes/659/meat-and-poultry/chicken/chicken-breasts/'#, # chicken breasts
            #'http://allrecipes.com/recipes/78/breakfast-and-brunch/' # breakfasts with eggs
    ]

    def parse(self, response):
        def uniquify(list):
            # not order preserving, but quick - taken from https://www.peterbe.com/plog/uniqifiers-benchmark
            set = {}
            map(set.__setitem__, list, [])
            return set.keys()

        ## TODO: change to use XPath selectors?    

        #num_recipes = 0
        links = response.css('article.grid-col--fixed-tiles a::attr(href)').re(r'^\/recipe\/.*$') # finds only links that start with '/recipe/'
        #links = response.xpath('//*/@href').re(r'^\/recipe\/.*$')
        links = uniquify(links) # returns only unique values in list

        for i in range (0, len(links)):
            links[i] = urlparse.urljoin(response.url, links[i])

        if len(links) >= 5:
            num_recipes = 5
        else:
            num_recipes = len(links)

        rand_recipes = random.sample(links, 5)

        # yield {
        #     'relative_links': rand_recipes,
        #     'length': len(links)
        # }

        ## TODO: follow each random link and parse info from them for emailing
        for recipe in rand_recipes:
            yield Request(recipe, callback=self.parse_following_urls)
    #     ## TODO: create separate file-parsing + email script
    #     ## TODO: separate script for pulling ingredients out to make a shopping list of sorts

        
    def parse_following_urls(self, response):
        l = IL(item=AllrecipesItem(), response=response)

        # load fields using XPath expressions
        l.add_xpath('title', '//h1[@itemprop="name"][1]/text()')
        l.add_xpath('ingredients', '//span[@itemprop="ingredients"]/text()')
        l.add_xpath('directions', '//span[@class="recipe-directions__list--item"]/text()')
        l.add_xpath('recipe_yield_value', '//span[@class="servings-count"][1]/text()') # broken
        l.add_xpath('recipe_yield_units', '//*[@id="servings-button"]/span[1]/span[2]/text()')
        l.add_xpath('cals_per_serving', '//*[@id="nutrition-button"]/span[1]/span[1]/text()')
        l.add_xpath('cook_time', '//span[@class="ready-in-time"][1]/text()')

        # housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()






