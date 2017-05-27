#!/usr/bin/python3

from model import *  
import jieba
import jieba.analyse
jieba.load_userdict("userdict.txt")
import types 
import pymysql
import json
import re
import requests

def filterWord(word):
    '''   过滤不符合要求的词  '''
    p = re.compile('[a-zA-Z0-9]+') 
    if ( len(word) < 2 or p.match(word)) :
        return False
    return True

def dict2list(dic:dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst


def color(ws) :
    ''' 判断颜色词语 '''
    ps = ['黑', '白', '藍', '褐', '淡','灰','青','粉','紫', '銀','綠','黃','銅','薰衣草','銹','橙','墨', '紅']
    p = re.compile("|".join(ps))
    for w in ws:
        if(p.match(w[0])) :
            print ("%s; %s" %(w[0], w[1]))

def tfidf(notes) :
    words = jieba.analyse.extract_tags(notes, 500, True, ())
    for word in words:
        if(not filterWord(word[0])):
            continue
        value = int(word[1] * 1000)
        print ("%s; %s" %(word[0], value))

def textrank(notes) :
    for x, w in jieba.analyse.textrank(notes, 500, withWeight=True):
        value = int(w * 100)
        print('%s;%s;;;;0' % (x, value))

lots = session.query(Lot).filter(Lot.secondary_title.like('%趙無極%')).all()
#lots = session.query(Lot).all()
notes = ""
for lot in lots:
    notes += lot.notes.replace(' ','')

tfidf(notes)

'''
p = re.compile('[a-zA-Z0-9]+') 
words = jieba.lcut(notes)
ws = {}
for word in words : 
    if ( len(word) < 2 or p.match(word)) :
        continue
    if(not word in ws) :
        ws[word] = 0
    ws[word] += 1


ws = sorted(dict2list(ws), key=lambda x:x[1], reverse=True)
color(ws)
'''

#for w in ws :
#    print (w[1],w[0])

#print("Full Mode: " + "/ ".join(words)) 
#print (jieba.analyse.extract_tags(notes, 50))

session.close()
