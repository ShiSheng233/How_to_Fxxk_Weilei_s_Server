# -*- coding: UTF-8 -*-
import random
import requests

#url -> "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=Ta%s&words=%s&nickname=%s<img src='2131099769'>"%(room_id,uid,words,name)
namelist = ["超爱xwz","漩涡鸣人","一个正直的人","卢本伟","蕾哥","内阁首辅","多好看的ui","皮卡丘","九黎","开发者","测试用户","阿里云官方","味蕾专用测试账户","星空"]
gender = ["♂","♀"]
wordslist = ["这个软件做的真好啊","测试消息","这个sb东西都要付费？","wdnmd","味蕾就是个智障"]

proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}


while True:
    room_id = "客厅"
    name = namelist[random.randint(0,13)] + gender[random.randint(0,1)]
    words = wordslist[random.randint(0,4)]
    uid = random.randint(10000000,49999999999)
    request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=Ta%s&words=%s&nickname=%s<img src='2131099769'><img src='2131099769'><img src='2131099769'><img src='2131099769'><img src='2131099769'>"%(room_id,uid,words,name)
    requests.get(request_url, proxies=proxies)
    print("Done.\n")
