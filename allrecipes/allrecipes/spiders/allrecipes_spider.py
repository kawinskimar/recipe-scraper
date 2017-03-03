import scrapy
import random
import urlparse

class AllrecipesSpider(scrapy.Spider):
    name = 'allrecipes'
    allowed_domains = ['allrecipes.com']
    download_delay = 1

    start_urls = [
            # American recipe categories
            'http://allrecipes.com/recipes/659/meat-and-poultry/chicken/chicken-breasts/'#, # chicken breasts
            #'http://allrecipes.com/recipes/148/breakfast-and-brunch/eggs/' # breakfasts with eggs
    ]

    def parse(self, response):
        def uniquify(list):
            # not order preserving, but quick - taken from https://www.peterbe.com/plog/uniqifiers-benchmark
            set = {}
            map(set.__setitem__, list, [])
            return set.keys()

        links = response.css('article.grid-col--fixed-tiles a::attr(href)').re(r'^\/recipe\/.*$') # finds only links that start with '/recipe/'
        links = uniquify(links) # returns only unique values in list

        for i in range (0, len(links)):
            links[i] = urlparse.urljoin(response.url, links[i])

        rand_recipes = random.sample(links, 5)

        ## TODO: follow each random link and parse info from them for emailing
        ## TODO: create separate file-parsing + email script
        ## TODO: separate script for pulling ingredients out to make a shopping list of sorts

        yield {
            'relative_link': rand_recipes
        }




