# How to Fxxk Weilei's Server

## 介绍一下这个app

### 他有什么用？
占内存、锻炼眼睛、浪费流量、泄露隐私
开发者正在快速迭代升级中，更多~~好~~功能等你发现！
现在已经更新3.7，开发者为使用者的使用时间感到担忧，于是去掉了夜间模式！

## 准备
- 一台可以上网的电脑
- 一个神经中枢、运动中枢没有异常的大脑
- 任意一只视觉范围在30cm的眼睛
- 任意一只可正常活动的手

## 原理
由于更新了接口，现在稍微有些复杂，需要对下面这个链接发送**GET请求**：
> http://zhinengjiaju.vip/xczx/saidwords.action?roomid=房间号&uid=Ta用户ID&words=内容&nickname=用户名&timestamp=时间戳&salt=MD5

其中有几个数据，我们来分析一下。
1. 房间号
  - 魏先生软件的用户开通的房间名
  - e.g. 树洞 图书馆 ···
2. 用户ID
  - 9位至11位的数字，可以随便填
3. 内容
  - 字面意思，消息内容
4. 用户名
  - 字面意思，自己设置就好，发送不了消息请更换一个，魏雷很喜欢设置关键词
  - 用户名后面要跟上"♂"或者"♀"
5. 时间戳
  - 当前的13位unix时间戳
6. MD5
  - 本次更新的重头戏，以下是分析
    - 成分
    > roomid=房间号&uid=用户ID&words=内容&nickname=用户名&timestamp=时间戳&key=发送的key
    - 解析
      - roomid uid words nickname timestamp与上方一样，此处不再赘述
      - key
        - 本次的重要更新部分，据反向分析来看是从OSS上下载一个固定的txt，下面给出key
        > fnakdjsgangaj65984qdvcvo71as1a3ds1g56a1g5a1ggagra&gajg15615avasggsa66a15g651a71ger1g5ar1g56ytiu7

> 例子 GET http://zhinengjiaju.vip/xczx/saidwords.action?roomid=树洞&uid=TaMP450305303&words=你马没了！Сука блядь！С ука блядь！&nickname=优秀♂&timestamp=1584598451362&salt=4cd11a186023cb4623fd3c0a3d93406a


## 开始吧！
由于这次更新了md5，使用浏览器发包不再现实，请使用脚本进行发包测试

## 已知问题
1. 这次更新的VIP机制未知，还未分析
2. 当用户名内含有特殊字符时，是无法发送的
3. 服务端后台可能更新了内容审核，[造成返回ok，实则不显示的问题](https://github.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/issues/2)。

## 注意事项
经过我们几天的发包、攻击测试，发现服务器会限制多次发包的用户，建议两次发包间间隔5~13秒