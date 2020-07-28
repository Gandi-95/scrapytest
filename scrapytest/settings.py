# -*- coding: utf-8 -*-

# Scrapy settings for scrapytest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapytest'

SPIDER_MODULES = ['scrapytest.spiders']
NEWSPIDER_MODULE = 'scrapytest.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapytest (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapytest.middlewares.ScrapytestSpiderMiddleware': 543,
#}

# 设置IP池和用户UserAgent

#  禁止本地Cookie
COOKIES_ENABLED = False

# 设置用户代理池
UAPOOL = [
	"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scrapytest.middlewares.ScrapytestDownloaderMiddleware': 543,
   'scrapytest.middlewares.ProxyMiddleware': 543,
   # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
   # 'scrapytest.middlewares.IPPOOlS' : 125,
   # 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 2,
   #  'scrapytest.uamid.Uamid': 1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapytest.pipelines.ScrapytestPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXIES = [
'58.218.92.199:6416', '58.218.92.199:6280', '58.218.92.197:9272', '58.218.92.199:5242', '58.218.92.196:2829',
'58.218.92.196:5057', '58.218.92.198:2799', '58.218.92.199:6436', '58.218.92.198:5472', '58.218.92.198:6095',
'58.218.92.198:9486', '58.218.92.197:9635', '58.218.92.199:6057', '58.218.92.196:4213', '58.218.92.199:8992',
'58.218.92.199:7918', '58.218.92.198:4921', '58.218.92.198:5321', '58.218.92.199:8330', '58.218.92.199:6674',
'171.211.5.160:40230', '110.86.174.147:39114', '61.49.83.223:17816', '114.233.8.112:28803', '117.66.232.136:50186',
'114.233.8.94:28803', '112.250.211.57:40139', '139.213.2.92:39133', '49.88.90.219:28803', '125.94.165.17:43967',
'110.18.2.156:40547', '121.237.148.48:29553', '123.169.37.109:38023', '182.34.193.0:39603', '175.42.168.18:39332',
'175.149.220.143:12980', '114.106.195.139:31791', '117.92.147.118:28803', '119.39.219.228:44167', '119.132.66.74:28803'
]