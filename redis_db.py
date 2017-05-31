#coding=utf-8
'''
Created on May 7, 2017

@author: fate
'''
import redis
import uniout
r= redis.Redis(host='127.0.0.1', port=6379,db=0)
urls = ['https://search.jd.com/Search?keyword=洗衣机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=6&wq=洗衣机&page=1&s=1&click=0',
        'https://search.jd.com/Search?keyword=洗衣机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=6&wq=洗衣机&page=3&s=51&click=0', ]
for i in range(100):
    a=5+i*2
    b=110+i*60
    str_a=str(a)
    str_b=str(b)
    next_page='https://search.jd.com/Search?keyword=洗衣机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=6&wq=洗衣机&page='+str_a+'&s='+str_b+'&click=0'
    urls.append(next_page)
for url in urls:
    r.lpush('JD_start_urls',url)
    

        
