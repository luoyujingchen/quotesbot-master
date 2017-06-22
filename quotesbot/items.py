# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()

    url = scrapy.Field()
    useful_count = scrapy.Field()
    useless_count = scrapy.Field()

    pass
