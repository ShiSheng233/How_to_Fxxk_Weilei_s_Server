# -*- coding: UTF-8 -*-
import json
from os import system
from random import randint
from requests import get
from time import sleep

system("title Repeater")
print("Code by Fuck_WEILEI Team\n")
roomname = '客厅'
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
    get(request_url)
    print("Done.")

while True:
    sleep(randint(5,10))
    do()