#!/usr/bin/python3

import types 
import pymysql
import json
import requests

from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# 创建对象的基类:
Base = declarative_base()

# 定义Auction对象:
class Auction(Base):
    # 表的名字:
    __tablename__ = 'auctions'

    id = Column(Integer, primary_key=True)
    name = Column(String(500),nullable=False)
    number = Column(Integer)
    url = Column(String)
    is_show = Column(Integer)
    recommended = Column(Integer)
    banner = Column(String)
    thumbnail = Column(String)
    location_id = Column(Integer)
    lot_link = Column(String)
    introduction = Column(String)
    online_auction = Column(Integer)
    auto_relevant = Column(Integer)
    time_list = Column(String)
    contact_list = Column(String)
    preview_list = Column(String)
    relevant_list = Column(String)
    start_dateline = Column(Integer)
    end_dateline = Column(Integer)
    create_dateline = Column(Integer)
    update_dateline = Column(Integer)
    delete_dateline = Column(Integer)
    result_link = Column(String)
    sale_total = Column(String)

class Lot(Base):
    # 表的名字:
    __tablename__ = 'lots'

    id = Column(Integer, primary_key=True)
    auction_id = Column(Integer)
    primary_title = Column(String)
    secondary_title = Column(String)
    artist_maker = Column(String)
    number = Column(Integer)
    description = Column(String)
    image = Column(String)
    currency_type = Column(String)
    low_estimate = Column(Integer)
    high_estimate = Column(Integer)
    realized_price = Column(Integer)
    notes = Column(String)
    provenance = Column(String)
    exhibited = Column(String)
    literature = Column(String)
    pre_lot_text = Column(String)
    post_lot_text = Column(String)
    is_overseas = Column(Integer)
    withdraw = Column(Integer)
    estimate_on_request = Column(Integer)
    not_exportable = Column(Integer)
    special_notice = Column(String)
    create_dateline = Column(Integer)
    delete_dateline = Column(Integer)

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:@localhost:3306/auction?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()


