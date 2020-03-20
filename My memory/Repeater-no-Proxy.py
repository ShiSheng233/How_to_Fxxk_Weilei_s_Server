# -*- coding: UTF-8 -*-
import json
from os import system
from random import randint
from requests import get
from time import sleep

system("title Repeater")
print("Code by Fuck_WEILEI Team\n")
roomname = str(input("你想要启动复读的群组是:"))

def do():
    print("\n复读中...")
    o = get("https://zhinengjiaju.vip/xczx/gettalks.action?roomid=%s"%(roomname))
    data2 = o.json()['room']['talks']
    data3 = eval(str(data2[-1]))
    uid = data3['uid']
    name = data3['nickname']
    words = data3['words']
    request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=%s&words=%s&nickname=%s"%(roomname,uid,words,name)
    print("URL=%s\nROOM=%s\nUID=%s\nNAME=%s\nVIP=true\nWORDS=%s\n"%(request_url,roomname,uid,name,words))
    if "黑客" in words or "骇客" in words or "C群" in words or "c群" in words or "孤儿" in words or "脚本" in words:
        print("识别到对我方不友好文字，本次复读取消")
    else:
        get(request_url)
        print("Done.")

while True:
    sleeptime = randint(6,15)
    sleep(sleeptime)
    print("离上次复读过去了%d秒"%(sleeptime))
    do()

print()
print("程序非正常结束，IP可能被封禁，请更换IP再试\n")
input("回车两次以退出...")
input()