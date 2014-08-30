import scrapy

from capitaldata.items import InstitutionItem

class InstitutionSpider(scrapy.Spider):
	name = "institution"
	allowed_domains = ["itjuzi.com"]
	start_urls = ["http://itjuzi.com/investfirm?page=%s" % page for page in xrange(1,266)]
	# start_urls = ["http://itjuzi.com/investfirm/1352"]

	def parse(self, response):
		for sel in response.xpath('//div[contains(@class, "investfirm-list")]/div[@class="media"]'):
			url = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/@href').extract()[0]
			name = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/text()').extract()[0]
			yield scrapy.Request(url, callback=self.parseInstitution, meta={'name':name})

	def parseInstitution(self, response):
		for sel in response.xpath('//div[contains(@class, "person-info")]/div[@class="media"]'):
			item = InstitutionItem()
			item['name'] = response.meta['name']
			item['avatar'] = sel.xpath('a/img/@src').extract()
			#item['name'] = sel.xpath('ul[contains(concat(" ", normalize-space(@class), " "), " media-body ")]/li[1]/a/text()').extract()
			item['website'] = sel.xpath('div[@class="media-body"]/ul/li[1]/a/@href').extract()
			item['phases'] = sel.xpath('div[@class="media-body"]/ul/li[2]//a/text()').extract()
			item['fields'] = sel.xpath('div[@class="media-body"]/ul/li[3]//a/text()').extract()
			item['description'] = sel.xpath('div[@class="media-body"]/ul/li[4]/em/text()').extract()
			yield item
