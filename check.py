#!/usr/bin/python3

import types 
import pymysql
import json
import requests

start = 849918721697914880;
for i in range(800000000000156164, 849918721697914884) :
    url = "http://mp.weixinhost.com/addon/christies-wesite?a=get_mslp_detail&id=" + str(i)
    try:
        response = requests.get(url,  timeout = 10)
        result = json.loads(response.text)
        print (result['err_code'], i)
    except Exception as e:
        print (2, i)
