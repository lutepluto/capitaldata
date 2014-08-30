# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InstitutionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    images = scrapy.Field()

    name = scrapy.Field()
    avatar = scrapy.Field()
    website = scrapy.Field()
    phases = scrapy.Field()
    fields = scrapy.Field()
    description = scrapy.Field()

class MyItem(scrapy.Item):

	images = scrapy.Field()
	avatar = scrapy.Field();
