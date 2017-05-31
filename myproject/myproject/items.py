# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class JDItem(scrapy.Item):
    # define the fields for your item here like:
    crawled =scrapy.Field()
    spider = scrapy.Field()
    item_id =scrapy.Field()
    item_url=scrapy.Field()
    profile=scrapy.Field()
    shop=scrapy.Field()
    shop_url=scrapy.Field() 
    flag=scrapy.Field()
    price=scrapy.Field()
# class JDItem(scrapy.Item):
	

