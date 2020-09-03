# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #新闻标题
    link = scrapy.Field() #新闻链接



class DetailsItem(scrapy.Item): #进入链接后爬取的信息
    author = scrapy.Field() #作者
    date = scrapy.Field() #日期
    num = scrapy.Field() #点击量


