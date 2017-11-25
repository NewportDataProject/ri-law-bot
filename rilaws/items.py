# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RilawsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Section(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    chapter = scrapy.Field()
    section = scrapy.Field()
    subject = scrapy.Field()
    history = scrapy.Field()
    text = scrapy.Field()
