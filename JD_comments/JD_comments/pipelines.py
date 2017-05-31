# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time
# class JDCommentsPipeline(object):
#     def open_spider(self, spider):
#     	self.file1=open('JD_comments.jl', 'a')
#     	self.file2=open('JD_comments.json','a')
#     	self.file2.write('[\n')
#     def process_item(self,item,spider):  

#     	str_line1=json.dumps(dict(item)) + "\n"
#     	self.file1.write(str_line1)
#     	str_line2=json.dumps(dict(item))+','+'\n'
#     	self.file2.write(str_line2)

#     	return item
#     def close_spider(self,spider):
#     	self.file1.close()
#     	self.file2.write(']')
#     	self.file2.close() 
class JDPipeline(object):
    def process_item(self, item, spider):
        ISOTIMEFORMAT='%Y-%m-%d %X'
        item["crawled"]=time.strftime(ISOTIMEFORMAT,time.localtime())
        item["spider"] = spider.name
        return item 

