# -*- coding: UTF-8 -*-
import random
import requests

#url -> "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=Ta%s&words=%s&nickname=%s<img src='2131099769'>"%(room_id,uid,words,name)

wordslist = ["这个软件做的真好啊","测试消息","这个sb东西都要付费？","wdnmd","味蕾就是个智障"]
namelist = [" ","超爱xwz","漩涡鸣人","一个正直的人","卢本伟","蕾哥","内阁首辅","多好看的ui","皮卡丘","九黎","开发者","测试用户","阿里云官方","味蕾专用测试账户","星空"]
room = ["客厅","树洞","月曦阁","泳池","被窝夜谈","图书馆","大明王朝","111","清王朝","晓","清","白虎堂","黑白无常","树洞避难所","爆破组"]
gender = ["♂","♀"]
vip = ["Yes","No"]
while True:
    room_id = room[random.randint(0,14)]
    name = namelist[random.randint(0,14)] + gender[random.randint(0,1)]
    words = wordslist[random.randint(0,4)]
    uid = random.randint(10000000,99999999999)
    vip_novip = vip[random.randint(0,1)]
    if vip_novip == "Yes":
        request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=Ta%s&words=%s&nickname=%s<img src='2131099769'>"%(room_id,uid,words,name)
        print("url=%s\nroom=%s\nuid=%d\nname=%s\nvip=true\nnwords=%s"%(request_url,room_id,uid,name,words))
        requests.get(request_url)
        print("Done.\n")
    else:
        request_url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=Ta%s&words=%s&nickname=%s"%(room_id,uid,words,name)
        print("url=%s\nroom=%s\nuid=%d\nname=%s\nvip=false\nwords=%s"%(request_url,room_id,uid,name,words))
        requests.get(request_url)
        print("Done.\n")
