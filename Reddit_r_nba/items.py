# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class RedditRNbaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   	title = Field()
   	author = Field()
   	number_of_comments = Field()
   	score_dislikes_full = Field()
   	score_dislikes_numbers = Field()
   	score_unvoted_full = Field()
   	score_unvoted_numbers = Field()
   	score_likes_full = Field()
   	score_likes_numbers = Field()
   	time_submitted_ago = Field()