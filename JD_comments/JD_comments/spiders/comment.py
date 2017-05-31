#coding=utf-8
'''
Created on Apr 16, 2017

@author: fate
'''
import scrapy
import json
import re
# import base64
import uniout
from scrapy_redis.spiders import RedisSpider
# import random
from JD_comments.items import JDCommentsItem
class CommentSpider(RedisSpider):
    # proxy_list=['http://42.123.91.247:16816','http://122.200.84.12:8080','http://60.174.237.43:9999']
    
    # commentspagenum=10
    pagecommentsnum=30
    name='comments'
  
    redis_key='comment_start_urls'
    # def start_requests(self):
    #     # proxy='http://42.123.91.247:16816'
        
    #     file_object = open('/Users/fate/Documents/myproject/myproject/spiders/JD_items.json')
    #     try:
    #         all_the_file = file_object.read()
    #         arr = json.loads(all_the_file)
    #         for a in arr:
    #             item_id=a['item_id']
    #             for i in range(self.commentspagenum):
    #                 i=i+1
    #                 comments_url='http://club.jd.com/review/'+item_id+'-1'+'-'+str(i)+'-0.html'
    #                 if not self.flag:
    #                     self.flag=['1']
    #                     break
    #                 yield scrapy.Request(comments_url,callback=self.parse)
    #                 # proxy_user_pass = '1452040900:gtmln55a'
    #                 # # setup basic authentication for the proxy
    #                 # encoded_user_pass = base64.encodestring(proxy_user_pass)
    #                 # req.meta['proxy']=random.choice(self.proxy_list)
    #                 # req.headers['Proxy-Authorization']='Basic ' + encoded_user_pass
    #                 # yield req                     
    #     finally:
    #         file_object.close()
            
    def parse(self,response):
        # print response.request.meta['proxy']
        request_inf=response.url
        # print request_inf
        pattern1=re.compile(r'(?<=-1-)\d{1,2}')
        pattern2=re.compile(r'(?<=review/)\d+')
        
        item_id=pattern2.search(request_inf).group()
        page=pattern1.search(request_inf).group()    
#         item_url=response.xpath('//li[@class="p-name"]/a/@href').extract_first()
#         pattern=re.compile(r'\d+')
#         idlist=pattern.findall(item_url)
#         for i in idlist:
#             item_id=i
        for i in range(0,self.pagecommentsnum):
            content=[]
            # tags=[]
            # # comments={}                      
            comment_id='comment-'+str(i+1)
            div=response.xpath('//div[@id="comment-'+str(i)+'"]')      
            user_name=div.xpath('.//div[@class="i-item"]/@data-nickname').extract_first()
            # if user_name is not None:
            #     user_name=user_name.strip()               
            star_num=div.xpath('.//span[contains(@class,"star")]/@class').extract_first()
            comment_date=div.xpath('.//span[@class="date-comment"]/a/text()').extract_first()
            if comment_date is not None:
                comment_date=comment_date.strip()

            for zz in div.xpath('.//dl'):
                content_type=zz.xpath('.//dt/text()').extract_first()
                if content_type is not None:
                    content_type=content_type.strip()
                description=zz.xpath('.//dd/text()').extract_first()
                if description is not None:
                    description=description.strip()
                cell=content_type+description
                content.append(cell)
            tags=div.xpath('.//span[@class="comm-tags"]/span/text()').extract()
            if tags is not None:
                for i in tags:
                    content[0]=content[0]+i+','               
            flag=content
            if not flag :
                break
            JD_comment=JDCommentsItem()
            JD_comment['item_id']=item_id
            JD_comment['page']=page
            JD_comment['comment_id']=comment_id
            JD_comment['user_name']=user_name
            JD_comment['star_num']=star_num
            JD_comment['content']=content
            JD_comment['comment_date']=comment_date

            yield JD_comment


            # {
            #         'item_id':item_id,
            #         'page':page,
            #         'comment_id':comment_id,
            #         'user_name':user_name,
            #         'star_num':star_num,                           
            #         'content':content,
                                       
            #         }
                
                
                
        
  # request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"

  #   # Use the following lines if your proxy requires authentication
  #   proxy_user_pass = "USERNAME:PASSWORD"
  #   # setup basic authentication for the proxy
  #   encoded_user_pass = base64.encodestring(proxy_user_pass)
  #   request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass          
            
            
#             
#             dict={
#                 
#                 
#                 
#                 
#                 
#                 
#                 }
#         yield 
# #                 
#                 
#                 
#         yield{
#             'item_id':item_id,
#             'user_name':user_name,
#             'star_num':star_num,
#             'comment_date':comment_date,         
#             'content':content,                 
#             }
#     