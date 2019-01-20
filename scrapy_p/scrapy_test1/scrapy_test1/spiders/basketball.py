# -*- coding: utf-8 -*-
import scrapy
import re
import requests


class BasketballSpider(scrapy.Spider):
    name = 'basketball'
    allowed_domains = ['https://nba.stats.qq.com']
    start_urls = ['https://nba.stats.qq.com/player/list.htm']

    def parse(self, response):
        # print(response.url)
        # print(response.text)
        # print(dir(response))
        # print(response.request)
        # return response
        # print(response.body.decode("GBK"))
        filename = "basketball_player"
        with open(filename,"a+",encoding="utf-8") as file:
            file.write(response.body.decode("GBK"))

        # //div[@class="teams"]//tbody//span