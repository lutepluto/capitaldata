import scrapy

from capitaldata.items import InstitutionItem
from capitaldata.items import InvestEventItem
from capitaldata.items import InvestorItem
from capitaldata.items import CompanyItem

class InstitutionSpider(scrapy.Spider):
	name = "institution"
	allowed_domains = ["itjuzi.com"]
	start_urls = ["http://itjuzi.com/investfirm?page=%s" % page for page in xrange(1,268)]
	# start_urls = ["http://itjuzi.com/investfirm/1352"]

	def parse(self, response):
		for sel in response.xpath('//div[contains(@class, "investfirm-list")]/div[@class="media"]'):
			url = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/@href').extract()[0]
			name = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/text()').extract()[0]
			yield scrapy.Request(url, callback=self.parseInstitution, meta={'name':name, 'url':url})

	def parseInstitution(self, response):
		for sel in response.xpath('//div[contains(@class, "person-info")]/div[@class="media"]'):
			item = InstitutionItem()
			item['url'] = response.meta['url']
			item['name'] = response.meta['name']
			item['avatar'] = sel.xpath('a/img/@src').extract()
			item['website'] = sel.xpath('div[@class="media-body"]/ul/li[1]/a/@href').extract()
			item['phases'] = sel.xpath('div[@class="media-body"]/ul/li[2]//a/text()').extract()
			item['fields'] = sel.xpath('div[@class="media-body"]/ul/li[3]//a/text()').extract()
			item['description'] = sel.xpath('div[@class="media-body"]/ul/li[4]/em/text()').extract()
			yield item

class InvestEventSpider(scrapy.Spider):
	name = "investevent"
	allowed_domains = ['itjuzi.com']
	start_urls = ["http://itjuzi.com/investfirm?page=%s" % page for page in xrange(273, 275)]

	def parse(self, response):
		for sel in response.xpath('//div[contains(@class, "investfirm-list")]/div[@class="media"]'):
			url = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/@href').extract()[0]
			name = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/text()').extract()[0]
			yield scrapy.Request(url, callback=self.parseInvestEvent, meta={'name':name, 'url':url})

	def parseInvestEvent(self, response):
		for sel in response.xpath('//table[@id="company-member-list"]/tbody/tr'):
			item = InvestEventItem()
			item['url'] = response.meta['url']
			item['institution'] = response.meta['name']
			item['date'] = sel.xpath('td[1]/text()').extract()
			item['company'] = sel.xpath('td[2]/a/text()').extract()
			item['phase'] = sel.xpath('td[3]/a/text()').extract()
			item['total'] = sel.xpath('td[4]/text()').extract()
			item['field'] = sel.xpath('td[5]/a/text()').extract()
			item['investors'] = sel.xpath('td[6]//a/text()').extract()
			yield item

class InvestorSpider(scrapy.Spider):
	name = "investor"
	allowed_domains = ['itjuzi.com']
	start_urls = ["http://itjuzi.com/investor?page=%s" % page for page in xrange(1, 56)]

	def parse(self, response):
		for sel in response.xpath('//div[contains(@class, "person-list")]/div[@class="media"]/div[@class="media-body"]'):
			url = sel.xpath('h4[@class="media-heading"]/a/@href').extract()[0]
			name = sel.xpath('h4[@class="media-heading"]/a/text()').extract()[0]
			yield scrapy.Request(url, callback=self.parseInvestor, meta={'name':name, 'url':url})

	def parseInvestor(self, response):
		for sel in response.xpath('//article[@class="two-col-big-left"]'):
			item = InvestorItem()
			item['url'] = response.meta['url']
			item['name'] = response.meta['name']
			item['avatar'] = sel.xpath('div[1]/div/a/img/@src').extract()
			item['institution'] = sel.xpath('div[1]/div/div/ul/li[1]/a/text()').extract()
			item['title'] = sel.xpath('div[1]/div/div/ul/li[1]/text()').extract()
			item['weibo'] = sel.xpath('div[1]/div/div/ul/li[2]/a/text()').extract()
			item['description'] = sel.xpath('div[1]/div/div/ul/li[3]/em/text()').extract()
			item['province'] = sel.xpath('div[2]/ul/li[1]/a/text()').extract()
			item['city'] = sel.xpath('div[2]/ul/li[1]/em/text()').extract()
			item['jobs'] = sel.xpath('div[2]/ul/li[2]//a/text()').extract()
			item['education'] = sel.xpath('div[2]/ul/li[3]//a/text()').extract()
			item['fields'] = sel.xpath('div[2]/ul/li[4]//a/text()').extract()
			yield item

class CompanySprider(scrapy.Spider):
	name = "company"
	allowed_domains = ['itjuzi.com']
	start_urls = ['http://itjuzi.com/investfirm?page=%s' % page for page in xrange(273, 275)]

	def parse(self, response):
		for sel in response.xpath('//div[contains(@class, "investfirm-list")]/div[@class="media"]'):
			url = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/@href').extract()[0]
			name = sel.xpath('ul[contains(@class, "detail-info")]/li[1]/a/text()').extract()[0]
			yield scrapy.Request(url, callback=self.parseInvestEvent)

	def parseInvestEvent(self, response):
		for sel in response.xpath('//table[@id="company-member-list"]/tbody/tr'):
			url = sel.xpath('td[2]/a/@href').extract()[0]
			name = sel.xpath('td[2]/a/text()').extract()[0]
			yield scrapy.Request(url, callback=self.parseCompany, meta={'name':name})

	def parseCompany(self, response):
		for sel in response.xpath('//article[@class="two-col-big-left"]'):
			item = CompanyItem()
			item['name'] = response.meta['name']
			item['avatar'] = sel.xpath('//img[@id="company_big_show"]/@src').extract()[0]
			item['website'] = sel.xpath('div[2]/ul/li[1]/a/text()').extract()[0]
			item['establishDate'] = sel.xpath('div[2]/ul/li[3]/em/text()').extract()[0]
			item['location'] = sel.xpath('div[2]/ul/li[4]/a/text()').extract()[0]
			item['phase'] = sel.xpath('div[2]/ul/li[6]/a/text()').extract()[0]
			item['description'] = sel.xpath('div[2]/ul/li[9]/em/text()').extract()[0]
			yield item