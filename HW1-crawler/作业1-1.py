import re
import urllib.request

data = urllib.request.urlopen("http://www.ucas.ac.cn/XXGK").read()
data2 = data.decode("utf-8")

pat_email = '<p>Email：(.*?)</p>' #读取邮箱
email = re.compile(pat_email).findall(data2)

pat_tel = '<p>电话：(.*?)</p>' #读取电话
tel = re.compile(pat_tel).findall(data2)

pat_LXtel = '<div class="gksq">([\s\S]*?)</div>'  #先找联系电话所在框体
LXtel = re.search(pat_LXtel,data2)
LXtel2 = re.compile(pat_tel).findall(LXtel.group(0)) #再从框体中找到联系电话

pat_TStel = '<div class="gksq tsjd">([\s\S]*?)</div>'  #先找投诉电话所在框体
TStel = re.search(pat_TStel,data2)
TStel2 = re.compile(pat_tel).findall(TStel.group(0)) #再从框体中找到投诉电话

print(email)
print(tel)
print(LXtel2)
print(TStel2)
