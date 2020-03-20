#!/usr/bin/env python3
# coding=utf-8
import json
import urllib
import urllib.request
import urllib.parse
import time
import math


def get_reply(room):
    try:
        request = urllib.request.Request("https://zhinengjiaju.vip/xczx/gettalks.action?roomid=" + urllib.request.quote(room))
        response = urllib.request.urlopen(request)
        response = json.loads(response.read().decode('utf-8'))
        return response
    except Exception:
        return None


def send_reply(position):
    global cookie
    print("fa1。。。。" + str(position))

    header = {
        'Referer': 'https://www.bilibili.com/',
        'Cookie': cookie[position][0],
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    data = {
        "oid": 5094241,
        "type": 12,
        "rpid": 2519363636,
        "action": 1,
        "jsonp": "jsonp",
        "csrf": cookie[position][1]
    }
    print(data["rpid"])
    postdata = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request('https://api.bilibili.com/x/v2/reply/hate', data=postdata, headers=header, method='POST')
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))


if __name__ == "__main__":
    while True:
        room_id = input("输入房间名称：")
        reply_json = get_reply(room_id)
        if reply_json is None:
            print("无此房间！\n")
            continue
        with open("log/" + room_id + time.strftime("_%y-%m-%d-%H-%M-%S", time.localtime(time.time())) + ".txt", "w", encoding="utf-8") as file:
            file.write(json.dumps(reply_json, ensure_ascii=False))
        reply_json = reply_json["room"]
        pw = reply_json["psw"] if "psw" in reply_json else ""
        for i in range(len(reply_json["talks"])):
            time_reply = time.strftime("%y-%m-%d %H:%M:%S  ", time.localtime(reply_json["talks"][i]["time"] / 1000))
            nickname = "匿名" if ("nickname" not in reply_json) else reply_json["talks"][i]["nickname"]
            print(str(i+1) + "  " + time_reply + nickname + "(" + reply_json["talks"][i]["uid"] + ")：" + reply_json["talks"][i]["words"])
            if i % 20 == 19:
                print("第" + str(int(i / 20) + 1) + "页，共" + str(math.ceil(len(reply_json["talks"])/20)) + "页，密码：" + (pw if pw != "" else "无"))
                input("")
        print("第" + str(math.ceil(len(reply_json["talks"])/20)) + "页，共" + str(math.ceil(len(reply_json["talks"])/20)) + "页，密码：" + (pw if pw != "" else "无"))
