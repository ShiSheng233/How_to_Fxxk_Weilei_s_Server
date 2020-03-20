# -*- coding: UTF-8 -*-
import requests
import json
import time

roomname = "客厅"


while True:
    time.sleep(1)
    o = requests.get("https://zhinengjiaju.vip/xczx/gettalks.action?roomid=%s"%(roomname))
    data2 = o.json()['room']['talks']
    data3 = eval(str(data2[-1]))
    uid = data3['uid']
    name = data3['nickname']
    words = data3['words']
    print()
    print(uid)
    print(name)
    request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=Ta%s&words=%s&nickname=%s<img src='2131099769'>"%(roomname,uid,words,name)
    print("url=%s\nroom=%s\nuid=%s\nname=%s\nvip=true\nwords=%s\n"%(request_url,roomname,uid,name,words))
    requests.get(request_url)
    print("Done.\n")