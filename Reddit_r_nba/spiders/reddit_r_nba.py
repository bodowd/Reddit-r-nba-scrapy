# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from Reddit_r_nba.items import RedditRNbaItem


class RedditRNbaSpider(CrawlSpider):
    name = "reddit_r_nba"
    allowed_domains = ["www.reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/nba',
    )

    rules = [
    	Rule(LinkExtractor(
    		allow=['/r/nba/\?count=\d*&after=\w*']),
    		callback='parse_item',
    		follow=True)
    ]

    def parse_item(self, response):

    	selector_list = response.css('div.thing')
    	
    	for selector in selector_list:
    		item = RedditRNbaItem()
    		item['title'] = selector.xpath('div/p[1]/a/text()').extract()
    		# tested xpath selectors with scrapy shell until it returned just the authors
    		# when using the shell, put // in front of div to actually get it to return
    		# the author, but in the code, don't put //, because it is in a for loop, searching
    		# each item in selector_list (I think)
    		item['author'] = selector.xpath('div[2]/p[2]/a/text()').extract()
    		yield item
