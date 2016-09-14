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

		# CSS: div class=entry unvoted/p class = title/ p class=tagline
		item['author'] = selector.xpath('div[2]/p[2]/a/text()').extract()
		item['number_of_comments'] = selector.xpath('div[2]/ul[1]/li[1]/a/text()').extract()
		item['score_dislikes_full'] = selector.xpath('div[1]/div[2]').extract()
		item['score_dislikes_numbers'] = selector.xpath('div[1]/div[2]/text()').extract()
		item['score_unvoted_full'] = selector.xpath('div[1]/div[3]').extract()
		item['score_unvoted_numbers'] = selector.xpath('div[1]/div[3]/text()').extract()
		item['score_likes_full'] = selector.xpath('div[1]/div[4]').extract()
		item['score_likes_numbers'] = selector.xpath('div[1]/div[4]/text()').extract()
		item['time_submitted_ago'] = selector.xpath('div[2]/p[2]/time/text()').extract()
			
		yield item
