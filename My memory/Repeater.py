# -*- coding: UTF-8 -*-
from requests import get
import json
from os import system

proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

system("title Repeater")
print("Code by Fuck_WEILEI Team\n")
roomname = str(input("你想要启动复读的群组是:"))
while True:
    print("\n复读中...")
    o = get("https://zhinengjiaju.vip/xczx/gettalks.action?roomid=%s"%(roomname))
    data2 = o.json()['room']['talks']
    data3 = eval(str(data2[-1]))
    uid = data3['uid']
    name = data3['nickname']
    words = data3['words']
    request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=%s&words=%s&nickname=%s"%(roomname,uid,words,name)
    print("URL=%s\nROOM=%s\nUID=%s\nNAME=%s\nVIP=true\nWORDS=%s\n"%(request_url,roomname,uid,name,words))
    get(request_url,proxies=proxies)
    get(request_url,proxies=proxies)
    print("Done.")