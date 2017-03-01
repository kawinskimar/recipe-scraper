import scrapy

class AllrecipesSpider(scrapy.Spider):
    name = "allrecipes"

    start_urls = [
            # American recipe categories
            'http://allrecipes.com/recipes/201/meat-and-poultry/chicken/',
            'http://allrecipes.com/recipes/148/breakfast-and-brunch/eggs/'
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'allrecipes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

