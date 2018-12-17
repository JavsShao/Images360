# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Images360Pipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        '''
        Mongodb数据库初始化
        :param mongo_url: 地址
        :param mongo_db: 数据库
        '''
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
