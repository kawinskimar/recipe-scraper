#! python

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
            'http://allrecipes.com/recipes/144/breakfast-and-brunch/breakfast-casseroles/', # breakfast casseroles
            'http://allrecipes.com/recipes/659/meat-and-poultry/chicken/chicken-breasts/', # chicken breasts
            'http://allrecipes.com/recipes/693/meat-and-poultry/turkey/ground/', # ground turkey
            'http://allrecipes.com/recipes/17504/world-cuisine/latin-american/mexican/main-dishes/', # Mexican main dishes
            'http://allrecipes.com/recipes/16767/world-cuisine/european/italian/main-dishes/', # Italian main dishes
            'http://allrecipes.com/recipes/17135/world-cuisine/asian/chinese/main-dishes/' # Chinese main dishes
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

        num_recipes = 3

        for i in range (0, len(links)):
            links[i] = urlparse.urljoin(response.url, links[i])

        rand_recipes = random.sample(links, num_recipes)
        
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
        l.add_xpath('recipe_yield', '//div[@class="subtext"][1]/text()') # broken
        l.add_xpath('cals_per_serving', '//*[@id="nutrition-button"]/span[1]/span[1]/text()')
        l.add_xpath('cook_time', '//span[@class="ready-in-time"][1]/text()')
        l.add_xpath('image', '/html/body/div[1]/div[2]/div/div[3]/section/div[1]/div/section[1]/span/a[1]/img/@src')

        # housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()






