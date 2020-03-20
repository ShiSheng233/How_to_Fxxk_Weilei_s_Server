# -*- coding: UTF-8 -*-
import json
from hashlib import md5
from os import system
from random import randint
from time import sleep, time
from requests import get

system("title Boomer")
print("Code by Fuck_WEILEI Team\n")
roomname = str(input("你想要启动刷屏的群组是:"))
print()
name = str(input("你想刷屏的人名是:"))
print()
words = str(input("你想刷屏的话是:"))
print()

getmd5 = md5()

key = 'fnakdjsgangaj65984qdvcvo71as1a3ds1g56a1g5a1ggagra&gajg15615avasggsa66a15g651a71ger1g5ar1g56ytiu7'

def do():
    unixtime = str(int(time() * 1000))
    print("\n刷屏中...\n")
    uid = randint(1000000,99999999999)
    md5_s = "roomid=%s&uid=%s&words=%s&nickname=%s&timestamp=%s&key=%s"%(roomname,uid,name,words,unixtime,key)
    md5_s_utf = md5_s.encode(encoding='utf-8')
    getmd5.update(md5_s_utf)
    md5 = getmd5.hexdigest()
    url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=%s&words=%s&nickname=%s&timestamp=%s&salt=%s"%(roomname,uid,words,name,unixtime,md5)
    a = get(url)
    print(a.text)
    print("\nDone.")

while True:
    sleeptime = randint(6,13)
    sleep(sleeptime)
    print("\n离上次刷屏过去了%d秒"%(sleeptime))
    do()

print()
print("程序非正常结束，IP可能被封禁，请更换IP再试\n")
input("回车两次以退出...")
input()
