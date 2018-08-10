#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : wxrobot.py
# @Author : YeHao
# @Contact : onehour60mins@163.com
# @Date : 2018/8/10 9:58
# @Desc : 

import itchat

import requests


def get_response(_info):
    # 图灵机器人
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': 'f22447f37439434882098af565415433',  # 机器人apikey
        'info': _info,
        'userid': 'wechat-robot',
    }

    r = requests.post(api_url, data=data).json()

    return r


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 自动回复消息的消息内容
    return 'Y.H\'s robot PuPiL:' + get_response(msg['Text'])['text']


itchat.auto_login(hotReload=True)
itchat.run()
