# -*- coding: utf-8 -*-
from urllib.parse import urlencode

import scrapy
from scrapy import Request


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        '''
        用来生成50次请求的网址
        :return:
        '''
        data = {'ch':'photography', 'listtype':'new'}
        base_url = 'https://image.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse())

    def parse(self, response):
        pass
