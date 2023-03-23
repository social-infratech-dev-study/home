import slack_sdk
import os

token = os.environ['IMHappy_SLACK_BOT_TOKEN'] #본인의 Slack Bot Token 입력
channel = '#10min-bot' #메시지를 보낼 Channel명 입력

def talk():  #slack bot massage
    client = slack_sdk.WebClient(token=token)
    client.chat_postMessage(channel=channel, text="I'm happy~!")
    
talk()
