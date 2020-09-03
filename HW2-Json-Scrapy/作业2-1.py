import json
import re
import requests

headers = {
'Referer':'https://www.ptpress.com.cn/shopping/index',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

url = 'https://www.ptpress.com.cn/bookinfo/getBookListForWS'
res = requests.post(url, headers=headers).content.decode()
json_data = json.loads(res)['data']
#print(json_data)
for book in json_data:
    name = book['bookName']
    author = book['author']
    price = book['price']
    print('name:'+str(name)+' '+'author:'+str(author)+' '+'price:'+str(price)+'元')


