# -*- coding: utf-8 -*-
import scrapy
import re
import requests


class BasketballSpider(scrapy.Spider):
    name = 'basketball'
    allowed_domains = ['nba.stats.qq.com']
    start_urls = ['https://nba.stats.qq.com/player/list.htm']

    def parse(self, response):
        print("111")
        print(response.url)
        print(dir(response))
        print(response.headers)
        print(dir(response.request))
        print(response.request.headers)
        # print(response.text)
        # print(dir(response))
        # print(response.request)
        # return response
        # print(response.body.decode("GBK"))
        # filename = "basketball_player"
        # with open(filename,"a+",encoding="utf-8") as file:
        #     file.write(response.body.decode("GBK"))
        # content = response.xpath('//div[@class="teams"]')
        # basketball_team = content.xpath('./table/tbody//span').extract()
        # # basketball_team =
        # # print(response.xpath('//div[@class="teams"]//tbody//span'))
        # print("1")
        # print(content)
        # print(basketball_team)
        # print(content.xpath('./table').extract())
        # print("2")
        # //div[@class="teams"]//tbody//span
        content = response.text
        print(content)
        # re.findall("")