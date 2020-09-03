# -*- coding: utf-8 -*-


import scrapy
import requests
from HW.items import HwItem, DetailsItem
from lxml import etree
from scrapy.http import Request


class UcasSpider(scrapy.Spider):
    name = 'ucas'
    allowed_domains = ['www.ucas.ac.cn']
    start_urls = ['http://www.ucas.ac.cn/']

    def parse(self, response):

        node_list = response.xpath("//ul[@class='news_list']/li")
        for node in node_list:
            item = HwItem()
            item['title'] = response.xpath("./a[@target='_blank']/@title").extract() #爬取标题
            item['link'] = response.xpath("./a[@target='_blank']/@href").extract() #爬取链接
            # item['author'], item['date'], item['num'] = selector.xpath("//ul[@class='b-ainf']/li/text()")
            yield item
            yield scrapy.Request(url=item['link'], callback=self.details) #将item['link']传递给detials

    def details(self, response):
        item = DetailsItem()
        item['author'] = response.xpath("//ul[@class='b-ainf']/li/text()")[0].extract() #爬取作者 text()第一段
        item['date'] = response.xpath("//ul[@class='b-ainf']/li/text()")[1].extract() #爬取作者 text()第二段
        item['num'] = response.xpath("//ul[@class='b-ainf']/li/text()")[2].extract() #爬取作者 text()第三段
        yield item

    #
    # def parse(self, response):
    #     item = DangdangItem()
    #     item["title"] = response.xpath("//a[@class='pic']/@title").extract()
    #     item["link"] = response.xpath("//a[@class='pic']/@href").extract()
    #     item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
    #     yield item
    #     for i in range(2, 10):   #多页
    #         url = "http://category.dangdang.com/pg"+str(i)+"-cp01.54.06.00.00.00.html"
    #         yield Request(url, callback = self.parse)
