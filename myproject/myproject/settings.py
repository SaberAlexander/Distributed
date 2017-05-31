# -*- coding: utf-8 -*-

# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myproject'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'
#redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
LOG_LEVEL = 'DEBUG'

# SPLASH_URL = 'http://127.0.0.1:8050'

# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
USER_AGENT_LIST='useragents.txt'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 50

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

# # Retry many times since proxies often fail
# RETRY_TIMES = 10
# # Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
DOWNLOADER_MIDDLEWARES = {
    

    # 'scrapy_splash.SplashCookiesMiddleware': 723,
    # 'scrapy_splash.SplashMiddleware': 725,
    # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,

    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware':90,
    # 'scrapy_proxies.RandomProxy': 100,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,

    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'myproject.random_useragent.RandomUserAgentMiddleware': 400

}

# # Proxy list containing entries like
# # http://host1:port
# # http://username:password@host2:port
# # http://host3:port
# # ...
# PROXY_LIST = '/Users/fate/Documents/myproject/myproject/proxy_list.txt'

# # Proxy mode
# # 0 = Every requests have different proxy
# # 1 = Take only one proxy from the list and assign it to every requests
# # 2 = Put a custom proxy to use in the settings
# PROXY_MODE = 0

# # If proxy mode is 2 uncomment this sentence :
# #CUSTOM_PROXY = "http://host1:port"


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'myproject.pipelines.JDselfsalePipeline': 200,
   # 'myproject.pipelines.XmlExportPipeline':None,
   'myproject.pipelines.JDPipeline': 300,
   'myproject.pipelines.RedisPipeline': 350,
   'scrapy_redis.pipelines.RedisPipeline': 400,
}
REDIRECT_ENABLED = False
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 180
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
AJAXCRAWL_ENABLED = True
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# FEED_FORMAT=jsonlines
# FEED_FORMAT:jsonlines

# FEED_URI='file:/Users/fate/Desktop/text.csv'

# FEED_FORMAT:jsonlines

# FEED_STORAGES = { 'file': None,s
# }
# FEED_EXPORTERS = { 'csv': None,
# }
REDIS_PARAMS = {'host':'redis','decode_responses':False}


