#!/usr/bin/env python
# -*- coding: utf-8 -*-

import slack_sdk
import os
from random import randrange


SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]  # 본인의 Slack Bot Token 입력
SLACK_CHANNEL = "#10min-bot"  # 메시지를 보낼 Channel명 입력


def getTodayDinnerMenu():
    # 어차피 고기야
    menus = ["치킨", "삼겹살", "곱창", "불고기", "찜닭"]
    return menus[randrange(menus.__len__())]


def sendSlackMessgae(slack_messege):  # slack bot massage
    slack_token = SLACK_TOKEN  # slack bot token
    channel = SLACK_CHANNEL  # chnnel for sending massege from slack bot
    message = slack_messege  # message from slack bot
    client = slack_sdk.WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=message)


# 메시지 발송
message = "와라라 저녁 뭐먹지 : "+getTodayDinnerMenu()  # 보낼 메시지 입력
sendSlackMessgae(message)
