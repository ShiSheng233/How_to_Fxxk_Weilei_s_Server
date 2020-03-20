# How to Fxxk Weilei's Server

## 介绍一下这个app

### 他有什么用？
占内存、锻炼眼睛、浪费流量、泄露隐私
开发者正在快速迭代升级中，更多~~好~~功能等你发现！

## 准备
- 一台可以上网的电脑
- 一个神经中枢、运动中枢没有异常的大脑
- 任意一只视觉范围在30cm的眼睛
- 任意一只可正常活动的手

## 原理
非常简单，只需要对下面这个链接发送**GET请求**：
> http://zhinengjiaju.vip/xczx/saidwords.action?roomid=房间号&Tauid=USER-ID&words=消息&nickname=用户名
其中有几个数据，我们来分析一下。
1. 房间号
  - 魏先生软件的用户开通的房间名
  - e.g. 树洞 图书馆 ···
2. USER-ID
  - 9位至11位的数字，可以随便填
3. 消息
  - 字面意思，消息内容
4. 用户名
  - 字面意思，自己设置就好，发送不了消息请更换一个，魏雷很喜欢设置关键词
5. 用户名后
  - 必须要有字符'♂'或'♀'，否则直接"封号"
> 例子 GET http://zhinengjiaju.vip/xczx/saidwords.action?roomid=树洞&Tauid=1145141541&words=测试&nickname=测试♂

你也可以直接访问这个[链接](http://zhinengjiaju.vip/xczx/saidwords.action?roomid=树洞&Tauid=1145141541&words=测试&nickname=测试♂)，也可以看到效果

## 开始吧！
只需要浏览器，你就能做到
跟上面的例子一样，依照请求格式填写，Enter即可
当然，写个程序循环发送请求也是极好的
玩得愉快~

## 注意事项
经过我们几天的发包、攻击测试，发现服务器