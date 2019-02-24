# -*- coding: utf-8 -*-
import scrapy


class LeetcodeCnSpider(scrapy.Spider):
    name = 'leetcode-cn'
    allowed_domains = ['leetcode-cn.com/']
    start_urls = ['https://leetcode-cn.com//']

    def parse(self, response):
        pass
