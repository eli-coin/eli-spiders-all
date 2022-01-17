# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Jb51Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    path = scrapy.Field()
    url = scrapy.Field()
    context = scrapy.Field()
    pass
