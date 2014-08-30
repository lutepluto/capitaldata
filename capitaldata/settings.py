# -*- coding: utf-8 -*-

# Scrapy settings for capitaldata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'capitaldata'

SPIDER_MODULES = ['capitaldata.spiders']
NEWSPIDER_MODULE = 'capitaldata.spiders'

ITEM_PIPELINES = {
	'capitaldata.pipelines.JsonWriterPipeline': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'capitaldata (+http://www.yourdomain.com)'
