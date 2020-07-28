# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()                #网址
    title = scrapy.Field()              #标题
    totle_price = scrapy.Field()        #总价
    price = scrapy.Field()              #每平米价
    down_paymen = scrapy.Field()        #首付
    monthly_house = scrapy.Field()      #月供
    residential = scrapy.Field()        #小区
    area = scrapy.Field()               #区域
    house_type = scrapy.Field()         #户型
    floor_area = scrapy.Field()         #建筑面积
    carpet_area = scrapy.Field()        #室内面积
    floor = scrapy.Field()              #楼层
    renovation = scrapy.Field()         #装修
    elevator = scrapy.Field()           #电梯
    construction_time = scrapy.Field()  #建筑时间
    pass