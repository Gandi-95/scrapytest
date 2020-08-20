# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class ScrapytestPipeline(object):

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(['url', 'title', 'totle_price', 'price', 'down_paymen', 'monthly_house', 'residential',
                        'area', 'house_type', 'floor_area', 'carpet_area', 'floor', 'renovation', 'elevator'])

    def process_item(self, item, spider):
        line = [item['url'], item['title'], item['totle_price'], item['price'], item['down_paymen'], item['monthly_house']
                , item['residential'], item['area'], item['house_type'], item['floor_area'], item['carpet_area'], item['floor']
                , item['renovation'], item['elevator']]
        self.ws.append(line)  # 按行添加
        self.wb.save('lianjia.xlsx')
        return item




