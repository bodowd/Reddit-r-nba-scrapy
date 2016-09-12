from scrapy import Item, Field


class RedditREpItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   	title = Field()
   	author = Field()