#!/usr/bin/python3

import types 
import pymysql
import json
import requests

# 打开数据库连接
db = pymysql.connect("localhost","root","","auction" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)
response = requests.get("http://mp.weixinhost.com/addon/christies-wesite?a=get_auction_detail&id=834669528423215104")
print(response.status_code) 
result = json.loads(response.text)
print (result)
response = requests.get("http://mp.weixinhost.com/addon/christies-wesite?a=get_lot_detail&id=860425591835466451");
result = json.loads(response.text)
print (result)

# 关闭数据库连接
db.close()
