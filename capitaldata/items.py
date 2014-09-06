# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import Join, TakeFirst

class InstitutionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()

    name = scrapy.Field()
    avatar = scrapy.Field()
    images = scrapy.Field()

    website = scrapy.Field()
    phases = scrapy.Field()
    fields = scrapy.Field()
    description = scrapy.Field()

class InvestEventItem(scrapy.Item):

	url = scrapy.Field()

	date = scrapy.Field()
	company = scrapy.Field()
	phase = scrapy.Field()
	total = scrapy.Field()
	field = scrapy.Field()
	investors = scrapy.Field()
	institution = scrapy.Field()

class InvestorItem(scrapy.Item):

	url = scrapy.Field()

	name = scrapy.Field()
	avatar = scrapy.Field()
	images = scrapy.Field()
	institution = scrapy.Field()
	title = scrapy.Field()
	weibo = scrapy.Field()
	description = scrapy.Field()
	province = scrapy.Field()
	city = scrapy.Field()
	jobs = scrapy.Field()
	education = scrapy.Field()
	fields = scrapy.Field()

class MyItem(scrapy.Item):

	images = scrapy.Field()
	avatar = scrapy.Field(output_processor=TakeFirst);
