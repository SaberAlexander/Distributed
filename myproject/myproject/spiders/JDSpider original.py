#coding=utf8
'''
Created on Mar 3, 2017

@author: fate
'''
import scrapy
from urlparse import urljoin
import uniout
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst, MapCompose, Join
from myproject.items import JDItem
# from scrapy_splash import SplashRequest
import re
import time
# from scrapy.spiders import Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy_redis.spiders import RedisCrawlSpider
from scrapy_redis.spiders import RedisSpider

class  JDSpider(RedisSpider):
    name='JDItems'
    redis_key='JD_start_urls'

    # rules = (
    #     # follow all links
    #     Rule(LinkExtractor(), callback='item_parse', follow=True),
    # )
             
    def parse(self,response):
        jd_item=JDItem()
        ls=response.xpath('//li[@data-sku]/@data-sku').extract()
        for urltail in ls:
            url=urljoin('https://item.jd.com/1665416.html',urltail)+'.html' 
            price=response.xpath('//li[@data-sku="'+urltail+'"]/div/div[@class="p-price"]/strong/@data-price').extract_first()     
            #url=urljoin('https://item.jd.com',urltail)
            jd_item['price']=price  
            request=scrapy.Request(url,callback=self.item_parse,)
            request.meta['item']=jd_item
            yield request


        # next_pages=[]
        # a=range(1,201,2)
        # b=range(1,5939,60)
         
        # for i in range(100):
        #     str_a=str(a[i])
        #     str_b=str(b[i])
        #     print str_a,str_b
        
            
           # time.sleep(10)
            
            
        # for new_url in next_pages:       
            
    def item_parse(self,response):
        jd_item=response.meta['item']
        item_url=response.url
        pattern=re.compile(r'\d+')
        idlist=pattern.findall(item_url)
        for i in idlist:
            item_id=i
        profile=response.xpath('//div[@class="sku-name"]/text()').extract_first()
        if profile is not None:
        	profile=profile.strip()
        
        shop=response.xpath('//div[@class="name"]/a/text()').extract_first()
        if shop is None:
            shop_temp=response.xpath('//div[@class="name"]')
            shop=shop_temp.xpath('string(.)').extract_first()
            shop="".join(shop.split())

        shop_url=response.xpath('//div[@class="name"]/a/@href').extract_first()
        
        temp=response.xpath('//em[@class="u-jd"]')# []为非京东自营返回值
        flag=temp.xpath('string(.)').extract_first()
        if flag is not None:
            flag=flag.strip()

        # price=response.xpath('//span[@class="p-price"]/span[@class]/text()').extract_first() 
        # if price is None:
        #     price=response.xpath('//span[@class="p-price"]/span[@class="p-price"]/span[@class]/text()').extract_first()

        
        jd_item['item_url']=item_url
        jd_item['item_id']=item_id
        jd_item['profile']=profile
        jd_item['shop']=shop
        jd_item['shop_url']=shop_url
        jd_item['flag']=flag

        yield jd_item
    
#         l = ItemstLoader(item=JDitem(), response=response):
#         l.add_value('item_id',item_id)
#         l.add_value('item_url',item_url)
#         l.add_xpath('profilr','//div[@class="sku-name"]/text()')
#         l.add_xpath('shop','//div[@class="name"]/a/text()')
#         l.add_value('flag',flage)
#         l.add_xpath('price','//span[@class="p-price"]/span[@class]/text()')
#         l.add_xpath('price','//span[@class="p-price"]/span[@class]/text()')
#         return l.load_item()


# class ItemstLoader(ItemLoader):

#     default_output_processor = TakeFirst()

#     name_in = MapCompose(unicode.title)
#     name_out = Join()

#     price_in = MapCompose(unicode.strip)
        # yield {
        #  'item_url':item_url,
        #  'item_id':item_id,
        #  'profile':profile,
        #  'shop':shop,
        #  'shop_url':shop_url,
        #  'flag':flag,
        #  'price':price,
        #      }

        
