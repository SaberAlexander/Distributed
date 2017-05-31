# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDSummariesItem(scrapy.Item):
	crawled =scrapy.Field()
	spider=scrapy.Field()

	SkuId=scrapy.Field()
	ProductId=scrapy.Field()
	Score5Count=scrapy.Field()
	Score4Count=scrapy.Field()
	Score3Count=scrapy.Field()
	Score2Count=scrapy.Field()
	Score1Count=scrapy.Field()
	ShowCount=scrapy.Field()
	CommentCount=scrapy.Field()
	AverageScore=scrapy.Field()
	GoodCount=scrapy.Field()
	GoodRate=scrapy.Field()
	GoodRateShow=scrapy.Field()
	GoodRateStyle=scrapy.Field()
	GeneralCount=scrapy.Field()
	GeneralRate=scrapy.Field()
	GeneralRateShow=scrapy.Field()
	GeneralRateStyle=scrapy.Field()
	PoorCount=scrapy.Field()
	PoorRate=scrapy.Field()
	PoorRateShow=scrapy.Field()
	PoorRateStyle=scrapy.Field()
	AfterCount=scrapy.Field()
    
