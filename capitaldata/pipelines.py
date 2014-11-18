# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import csv
import codecs

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

class JsonWriterPipeline(object):

	def __init__(self):
		self.file = codecs.open('institutions.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line.decode('unicode_escape'))
		return item

class CsvExportPipeline(object):

	def __init__(self):
		self.files = {}

	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline

	def spider_opened(self, spider):
		f = open('%s.csv' %  spider.name, 'w');
		self.files[spider] = f;
		self.exporter = CsvItemExporter(f, False)
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		f = self.files.pop(spider)
		f.close()

	def process_item(self, item, spoder):
		self.exporter.export_item(item)
		return item

class MyImagesPipeline(ImagesPipeline):

	def image_key(self, url):
		name = url.split('/')[-1]
		return 'full/%s' % (name)

	def get_media_requests(self, item, info):
		yield scrapy.Request(item['avatar'])

	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			raise DropItem("Item contains no images")
		item['images'] = image_paths
		return item