import requests
import re
from lxml import etree
import pymongo
import urllib.request

# MongoDB的连接
client = pymongo.MongoClient('localhost', 27017)
ucas = client['ucas']
report = ucas['HW2']

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
data = urllib.request.urlopen("http://www.ucas.ac.cn").read()
data2 = data.decode("utf-8")

pat = '<ul class="home-news-list" id="xwjj">([\s\S]*?)</ul>' #读取新闻聚焦板块内容
xwjj = re.compile(pat).findall(data2)
pat_news = '<a title=\"(.*?)\"'          #读取新闻标题
news_name = re.compile(pat_news).findall(xwjj[0])
pat_url = 'href=\"(.*?)\"'               #读取新闻链接
news_url = re.compile(pat_url).findall(xwjj[0])


def page_get(link):          #通过前面读取的链接，进入链接后爬取
    res = requests.get(link, headers).content
    selector = etree.HTML(res)
    title= selector.xpath('//title/text()')              #爬取标题
    data = selector.xpath('//ul[@class="b-ainf"]/li/text()')     #爬取作者日期阅读量
    author = ' '.join(data[0].split())        #因为网站格式，爬下来的数据有莫名的空格，通过此函数去掉，将大量空格改为单个空格
    date = ' '.join(data[1].split())
    num = ' '.join(data[2].split())
    report.insert_one({'title':title,'link':link,'author':author,'date':date,'num':num})#存入mongodb

#主函数
for i in range(len(news_url)):
    page_get(news_url[i])




