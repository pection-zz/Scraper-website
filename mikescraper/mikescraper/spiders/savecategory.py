# -*- coding: utf-8 -*-
import scrapy


class SavecategorySpider(scrapy.Spider):
    name = 'savecategory'
    allowed_domains = ['alibaba.com']
    start_urls = ['http://alibaba.com/']

    def parse(self, response):
        pass
