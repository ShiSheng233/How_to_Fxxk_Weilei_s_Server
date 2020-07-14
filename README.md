# How to Fxxk Weilei's Server

[![Python](https://img.shields.io/badge/Language-Python-green.svg)](https://python.org)
[![LICENSE](https://img.shields.io/badge/License-WTFPL-green.svg)](LICENSE)

[How to Fxxk Weilei's Server (English)](https://github.com/AkinoMaple/weartalk/blob/master/README.md)

> 据说魏雷要道歉，我在此声明，保留不撤回举报的权利
>
> 已经报送华为手表应用市场、小米手表应用市场、问问应用市场、工信部
>
> 举报的主要内容有：在未备案的情况下开通即时聊天服务、泄露用户隐私、色情、政治敏感等话题

**"腕上聊天室"APP已在华为手表应用市场、小米手表应用市场以及问问应用市场下架**

本仓库存放了我们用来测试的源码等，可以自己玩玩.

据开发者本人说，不会上架(由于举报而不能上架)到手表应用市场了，但可以通过ADB自行安装，现已推出国际版

我们已经将聊天室的聊天记录log上传至本仓库，详情请看[为什么要上传log](https://github.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/blob/master/chat_log/WHY_LOG.md)，或者打开[log存放路径](https://github.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/tree/master/chat_log)

## 魏雷简介

知名安卓开发者，高居[垃圾软件开发者名单第三位](https://t.me/lookatcoolapk/89)

熟练运用GET发送消息，不忘初心地使用了HTTP明文传输用户信息

拥有独特的审美观念，开发了许多令人作呕的Android Wear表盘，并声称"是拥有最全信息的表盘，前无古人，后无来者"

*是只会堆数据的表盘，也是最耗电的表盘，前无古人，后无来者*

## 介绍一下这个APP

### 它有什么用

占内存、锻炼眼睛、浪费流量、泄露隐私

开发者正在快速迭代升级中，更多~~好~~功能等你发现！

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

        - 重要更新部分，据反向后分析来看是从OSS上下载一个固定的txt，下面给出key

        > fnakdjsgangaj65984qdvcvo71as1a3ds1g56a1g5a1ggagra&gajg15615avasggsa66a15g651a71ger1g5ar1g56ytiu7

> 例子 GET http://zhinengjiaju.vip/xczx/saidwords.action?roomid=树洞&uid=TaMP450305303&words=你马没了！Сука блядь！С ука блядь！&nickname=优秀♂&timestamp=1584598451362&salt=4cd11a186023cb4623fd3c0a3d93406a

## 开始吧

由于这次更新了md5，使用浏览器发包不再现实，请使用脚本进行发包测试

## 已知问题

1. VIP在新版APP中变成订阅制
2. 当用户名内含有非UTF-8字符时无法发送
3. 服务端后台可能更新了内容审核，[造成返回ok，实则不显示的问题](https://github.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/issues/2)
4. VIP专属的头像更换功能我们暂未研究

## 注意事项

经过我们几天的发包、攻击测试，发现服务器会限制多次发包的用户，建议两次发包间间隔5~13秒，1分钟内发包不超过10次

## 提示

- 此软件在应用市场内不复存在，故本项目中的代码并不会持续有效
- 关于为什么会去举报、'攻击'，请了解整个事件
- 为什么要这么做？因为我在生活中遇到垃圾也会随手扔进垃圾桶
- 感谢与我一起干翻服务器的朋友们，谢谢你们

## 后记

- 事情结束了
- 我希望经历过这件事的朋友就当是看了场笑话，并请各位开发者引以为戒，这样的人品不可取
- 几天之内项目会转入Archive状态
- 魏雷先生关闭了该服务

## 证据&笑话

- 求软件被破解

![萎雷求被破解](https://raw.githubusercontent.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/master/%E8%AF%81%E6%8D%AE/%E6%B1%82%E8%A2%AB%E7%A0%B4%E8%A7%A3.png "求被破解")

- 伟大的魏雷软件帝国构想

![梦想](https://raw.githubusercontent.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/master/%E8%AF%81%E6%8D%AE/%E9%87%8E%E5%BF%83.png "梦想")

**u1s1，有能力使用海外版固件的用户，会用你这xx玩意？**

- 用户GHS，开发者不进行管理

![GHS1](https://raw.githubusercontent.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/master/%E8%AF%81%E6%8D%AE/GHS1.jpg "GHS-1")

![GHS2](https://raw.githubusercontent.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/master/%E8%AF%81%E6%8D%AE/GHS2.jpg "GHS-2")

- 公布被禁言用户IP地址

![IP](https://raw.githubusercontent.com/ShiSheng233/How_to_Fxxk_Weilei_s_Server/master/%E8%AF%81%E6%8D%AE/IP.jpg "公布IP地址")

