# -*- coding: utf-8 -*-
import scrapy

from scrapytest.items import LianjiaItem
import json
import random
import time

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    # allowed_domains = ['sz.lianjiao.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/']
    base_url = 'https://sz.lianjia.com'

    # python -m scrapy crawl lianjia -o items.json

    def parse(self, response):
        ul = response.xpath('//div[@class="info clear"]/div[@class="title"]')
        for li in ul:
            l = li.xpath('a[@class=""]/@href').extract()
            print(l[0])
            time.sleep(random.randint(0,2))
            yield scrapy.Request(url=l[0], callback=self.parse_house)

        # for i in range(3):
        #     l = ul[i].xpath('a[@class=""]/@href').extract()
        #     print(l[0])
        #     yield scrapy.Request(url=l[0], callback=self.parse_house)

        page_info = response.xpath('//div[@class="page-box fr"]/div[@class="page-box house-lst-page-box"]/@page-data').extract()
        res = json.loads(page_info[0])
        print(res)
        next_page = res['curPage']+ 1
        print(next_page)
        if next_page<= res['totalPage']:
            url = self.start_urls[0] + "pg"+str(next_page)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)



    def parse_house(self, response):
        item = LianjiaItem()
        print('----------------------------------------------------')
        item['url'] = response.url
        item['title'] = response.xpath('//div[@class="content"]/div[@class="title"]/h1/@title').extract()[0]
        item['totle_price'] = response.xpath('//span[@class="total"]/text()').extract()[0] + \
                              response.xpath('//span[@class="unit"]/span/text()').extract()[0]

        item['price'] = response.xpath('//div[@class="unitPrice"]/span[@class="unitPriceValue"]/text()').extract()[0] + response.xpath('//div[@class="unitPrice"]/span[@class="unitPriceValue"]/i/text()').extract()[0]
        shoufu = response.xpath('//div[@id="calculator"]/@data-shoufu').extract()[0]
        res = json.loads(shoufu)

        item['down_paymen'] = res['totalShoufuDesc']
        item['monthly_house'] = res['monthPayWithInterest']
        item['residential'] = response.xpath('//div[@class="communityName"]/a[@class="info "]/text()').extract()[0]

        area = response.xpath('//div[@class="areaName"]/span/a/text()').extract()
        item['area'] = area[0] + area[1]

        house_info = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li')
        item['house_type'] = house_info[1].xpath('./text()').extract()[0]
        item['floor_area'] = house_info[3].xpath('./text()').extract()[0]
        item['carpet_area'] = house_info[5].xpath('./text()').extract()[0]
        item['floor'] = house_info[2].xpath('./text()').extract()[0]
        item['renovation'] = house_info[9].xpath('./text()').extract()[0]
        item['elevator'] = house_info[10].xpath('./text()').extract()[0]
        # item['construction_time'] = response.xpath('//div[@class="areaName"]/span/a/text()').extract()


        yield item
