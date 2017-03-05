# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AllrecipesItem(Item):
    # defining all fields for item

    # primary fields
    title = Field()
    ingredients = Field()
    directions = Field()
    recipe_yield_value = Field() # not working
    recipe_yield_units = Field()
    cals_per_serving = Field() # not working
    cook_time = Field()

    # housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
