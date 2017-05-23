#!/usr/bin/python3

import types 
import pymysql
import json
import requests

start = 849918721697914880;
for i in range(800000000000133280, 870425591835468239) :
    url = "http://mp.weixinhost.com/addon/christies-wesite?a=get_lot_detail&id=" + str(i)
    try:
        response = requests.get(url)
        result = json.loads(response.text)
        print (result['err_code'], i)
    except Exception as e:
        print (2, i)
