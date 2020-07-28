# -*- coding: utf-8 -*-
import scrapy
import logging

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['test']
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        logging.info(response.text)

        temp = response.xpath('//*[@id="slider_w"]/div[1]/div/div[3]/div/text()').extract()
        logging.info(temp)
        pass
