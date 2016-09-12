# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from Reddit_r_nba.items import RedditRNbaItem


class RedditRNbaSpider(CrawlSpider):
    name = "reddit_r_nba"
    allowed_domains = ["reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/nba',
    )

    rules = [
    	Rule(LinkExtractor(
    		allow=['/r/nba/\?count=\d*&after=\w*']),
    		callback='parse_item',
    		follow=True)
    ]

    def parse(self, response):

    	selector_list = response.css('div.thing')
    	
    	for selector in selector_list:
    		item = RedditRNbaItem()
    		item['title'] = selector.xpath('div/p/a/text()').extract()
    		
    		yield item
