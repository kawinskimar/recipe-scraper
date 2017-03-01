import scrapy

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
        #links = response.css('article.grid-col--fixed-tiles a::attr(href)').re(r'^\/recipe\/.*$')
        #links = uniquify(links)

        yield {
            'relative_links': response.css('article.grid-col--fixed-tiles a::attr(href)').re(r'^\/recipe\/.*$')
            # TODO: find only links that start with '/recipe/'
            # TODO: remove duplicates from list of links
        }

    # not working the way I want it to
    def uniquify(list):
        # not order preserving, but quick - taken from https://www.peterbe.com/plog/uniqifiers-benchmark
        set = Set(list)
        return list(set)




