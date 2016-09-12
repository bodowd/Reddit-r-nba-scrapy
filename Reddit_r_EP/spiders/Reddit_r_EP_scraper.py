# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Reddit_r_EP.items import RedditREpItem


class RedditREpScraperSpider(CrawlSpider):
   name = "Reddit_r_EP_scraper"
   allowed_domains = ["reddit.com"]
   start_urls = (
        'http://www.reddit.com/r/EarthPorn',
    )

   rules = [
    	Rule(LinkExtractor(
    		allow=['/r/EarthPorn/\?count=\d*&after=\w*']),
    		callback='parse_item',
    		follow=True)
    ]

   def parse_item(self, response):

   	selector_list = response.css('div.thing')
    	
   	for selector in selector_list:
   		item = RedditREpItem()
   		item['title'] = selector.xpath('div/p[1]/a/text()').extract()
   		# tested xpath selectors with scrapy shell until it returned just the authors
   		# when using the shell, put // in front of div to actually get it to return
   		# the author, but in the code, don't put //, because it is in a for loop, searching
   		# each item in selector_list (I think)
   		item['author'] = selector.xpath('div[2]/p[2]/a/text()').extract()
   		yield item
