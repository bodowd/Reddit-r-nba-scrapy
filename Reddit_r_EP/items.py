from scrapy import Item, Field


class RedditREpItem(Item):
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