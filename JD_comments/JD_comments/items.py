# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDCommentsItem(scrapy.Item):
	crawled=scrapy.Field()
	spider=scrapy.Field()
	item_id=scrapy.Field()
	page=scrapy.Field()
	comment_id=scrapy.Field()
	user_name=scrapy.Field()
	star_num=scrapy.Field()
	comment_date=scrapy.Field()
	content=scrapy.Field()


    
