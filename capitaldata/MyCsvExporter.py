#!/usr/bin/python

from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class MyCsvExporter(CsvItemExporter):

	def serialize_field(self, field, name, value):
		if field == 'description':
			return value.strip().replace()