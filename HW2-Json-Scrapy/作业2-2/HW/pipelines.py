# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from HW.items import HwItem

class HwPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名称
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        # 创建数据库连接
        client = pymongo.MongoClient(host=host, port=port)
        # 指向指定数据库
        mdb = client['ucas']
        # 获取数据库里面存放数据的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]
    def process_item(self, item, spider):
        '''
            每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''
        if not item['title']:
            return item

        data = {
            'title': item['title'],
            'link': item['link'],
            'author':item['author'],
            'date':item['date'],
            'num':item['num']
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item



    #
    # def process_item(self, item, spider):
    #     data = dict(item)
    #     # 向指定的表里添加数据
    #     self.post.insert(data)
    #     return item
    #
    # def process_item(self, item, spider):
    #     client = pymongo.MongoClient('localhost', 27017)
    #     ucas = client['ucas']
    #     report = ucas['作业2']
    #
    #     for i in range(len(item['title'])):
    #         title = item['title'][i]
    #         link = item['link'][i]
    #         author = item['author'][i]
    #         date = item['date'][i]
    #         num = item['num'][i]
    #         report.insert_one({'标题': title, '作者': author, '日期': date, '阅读量': num, '链接': link})
    #
    #     return item
