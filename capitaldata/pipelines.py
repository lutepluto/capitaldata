# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class JsonWriterPipeline(object):

	def __init__(self):
		self.file = codecs.open('institutions.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line.decode('unicode_escape'))
		return item

class MyImagesPipeline(ImagesPipeline):

	def image_key(self, url):
		name = url.split('/')[-1]
		return 'full/%s' % (name)

	def get_media_requests(self, item, info):
		yield scrapy.Request(item['avatar'][0])

	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			raise DropItem("Item contains no images")
		item['images'] = image_paths
		return item