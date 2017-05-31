#coding=utf-8
'''
Created on Apr 16, 2017

@author: fate
'''
import scrapy
import json
import uniout
from scrapy_redis.spiders import RedisSpider
from JD_summaries.items import JDSummariesItem
# file_object = open(r'/Users/fate/Documents/myproject/myproject/spiders/JD_items.json')
# try:
#      all_the_file = file_object.read()
#      arr = json.loads(all_the_file)
#      for i,a in enumerate(arr):
#          print i,a['item_id']
# finally:
#      file_object.close()
# for i,a in enumerate(arr):
#          print i,a['item_id']
class SummarySpider(RedisSpider):
    name='summaries'
    redis_key='summary_start_urls'
    # def start_requests(self): 
    #     file_object = open('/Users/fate/Documents/myproject/myproject/spiders/JD_items.json')
    #     try:
    #         all_the_file = file_object.read()
    #         arr = json.loads(all_the_file)
    #         for a in arr:
    #             item_id=a['item_id']
    #             summmary_url='http://club.jd.com/ProductPageService.aspx?method=GetCommentSummaryBySkuId&referenceId='+item_id
    #             yield scrapy.Request(summmary_url, callback=self.summary_parse)
    #     finally:
    #         file_object.close()
     
                   
    def parse(self,response):
        summaryjson_dict=json.loads(response.body_as_unicode())
        summary_item=JDSummariesItem()
        # yield summaryjson_dict
        
        # item_id=summaryjson_dict.get()
        # comment_count=summaryjson_dict.get('CommentCount')
        # good_rate=summaryjson_dict.get('GoodRate')
        # score_1=summaryjson_dict.get('Score1Count')
        # score_2=summaryjson_dict.get('Score2Count')
        # score_3=summaryjson_dict.get('Score3Count')
        # score_4=summaryjson_dict.get('Score4Count')
        # score_5=summaryjson_dict.get('Score5Count')s
        SkuId=summaryjson_dict.get('SkuId')
        ProductId=summaryjson_dict.get('ProductId')
        Score5Count=summaryjson_dict.get('Score5Count')
        Score4Count=summaryjson_dict.get('Score4Count')
        Score3Count=summaryjson_dict.get('Score3Count')
        Score2Count=summaryjson_dict.get('Score2Count')
        Score1Count=summaryjson_dict.get('Score1Count')
        ShowCount=summaryjson_dict.get('ShowCount')
        CommentCount=summaryjson_dict.get('CommentCount')
        AverageScore=summaryjson_dict.get('AverageScore')
        GoodCount=summaryjson_dict.get('GoodCount')
        GoodRate=summaryjson_dict.get('GoodRate')
        GoodRateShow=summaryjson_dict.get('GoodRateShow')
        GoodRateStyle=summaryjson_dict.get('GoodRateStyle')
        GeneralCount=summaryjson_dict.get('GeneralCount')
        GeneralRate=summaryjson_dict.get('GeneralRate')
        GeneralRateShow=summaryjson_dict.get('GeneralRateShow')
        GeneralRateStyle=summaryjson_dict.get('GeneralRateStyle')
        PoorCount=summaryjson_dict.get('PoorCount')
        PoorRate=summaryjson_dict.get('PoorRate')
        PoorRateShow=summaryjson_dict.get('PoorRateShow')
        PoorRateStyle=summaryjson_dict.get('PoorRateStyle')
        AfterCount=summaryjson_dict.get('AfterCount')

        summary_item['SkuId']=SkuId
        summary_item['ProductId']=ProductId
        summary_item['Score5Count']=Score5Count
        summary_item['Score4Count']=Score4Count
        summary_item['Score3Count']=Score3Count
        summary_item['Score2Count']=Score2Count
        summary_item['Score1Count']=Score1Count
        summary_item['ShowCount']=ShowCount
        summary_item['CommentCount']=CommentCount
        summary_item['AverageScore']=AverageScore
        summary_item['GoodCount']=GoodCount
        summary_item['GoodRate']=GoodRate
        summary_item['GoodRateShow']=GoodRateShow
        summary_item['GoodRateStyle']=GoodRateStyle
        summary_item['GeneralCount']=GeneralCount
        summary_item['GeneralRate']=GeneralRate
        summary_item['GeneralRateShow']=GeneralRateShow
        summary_item['GeneralRateStyle']=GeneralRateStyle
        summary_item['PoorCount']=PoorCount
        summary_item['PoorRate']=PoorRate
        summary_item['PoorRateShow']=PoorRateShow
        summary_item['PoorRateStyle']=PoorRateStyle
        summary_item['AfterCount']=AfterCount

        return summary_item







#         yield 
#         {
#             'item_id':item_id,
#             'comment_count':comment_count,
#             'good_rate':good_rate,
#             'score1':score_1 ,
#             'score2':score_2 ,
#             'score3':score_3 ,
#             'score4':score_4 ,
#             'score5':score_5 ,                     
#             }      
     
     
     
        

        
    