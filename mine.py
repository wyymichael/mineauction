#!/usr/bin/python3

from model import *  
import jieba
import jieba.analyse
jieba.load_userdict("userdict.txt")
import types 
import pymysql
import json
import requests


lots = session.query(Lot).filter(Lot.secondary_title.like('%趙無極%')).filter(Lot.id == 796916965653614592).all()
#lots = session.query(Lot).all()
notes = ""
for lot in lots:
    notes += lot.notes.replace(' ','')

words = jieba.cut(notes)
print("Full Mode: " + "/ ".join(words)) 

#print (jieba.analyse.extract_tags(notes, 50))

session.close()
