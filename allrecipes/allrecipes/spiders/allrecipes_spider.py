import scrapy
import random

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

        rand_link = random.choice(links)

        yield {
            'relative_link': rand_link,
            'size': len(links)
        }

        ## TODO: follow random link (choose link at random from links list)




