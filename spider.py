#!/usr/bin/python3

from model import *  
import types 
import pymysql
import json
import requests

#http://mp.weixinhost.com/addon/christies-wesite?a=get_location_list   //所有地点的id
#http://mp.weixinhost.com/addon/christies-wesite?a=get_auction_list&count=20&end_dateline=&location_ids=&order=desc&start=280&start_dateline=&state=over

def requestUrl(url, timeout = 10) :
    response = requests.get(url, timeout = timeout)
    result = json.loads(response.text)
    return result

def saveLotFromAuction(auction_id) :
    total = 1;
    start = 0;
    count = 100
    while start < total :
        url = "http://mp.weixinhost.com/addon/christies-wesite?a=get_lot_list&count="+str(count)+"&start="+str(start)+"&auction_id=" + str(auction_id)
        print (url)
        result = requestUrl(url, timeout = 10)
        total = result['data']['total']
        if(not result['data']['list']) :
            continue
        for lot in result['data']['list'] :
            start += 1
            l = session.query(Lot).filter(Lot.id == lot['id']).first()
            if(not l) : 
                l = Lot()
                l.id = lot['id']
            for key in lot :
                setattr(l, key, lot[key])

            session.add(l)
            session.commit()

start = 0
while 1:
    url = "http://mp.weixinhost.com/addon/christies-wesite?a=get_auction_list&count=100&start=" + str(start)
    result = requestUrl(url, timeout = 10)
    if(not result['data']['list']) :
        break
    for auction in result['data']['list'] :
        start += 1
        a = session.query(Auction).filter(Auction.id == auction['id']).first()
        print (auction['id'])
        if(not a) : 
            a = Auction()
            a.id = auction['id']
        for key in auction :
            setattr(a, key, auction[key])

        session.add(a)
        session.commit()

        saveLotFromAuction(auction['id'])

#result = requestUrl("http://mp.weixinhost.com/addon/christies-wesite?a=get_mslp_detail&id=849918721697914880")

# 关闭session:
session.close()
