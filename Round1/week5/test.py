import requests
from datetime import datetime
import pandas as pd
import slack_sdk
import os

API_KEY = os.environ['API_KEY']
ADDRESS = os.environ['ADDRESS']

SLACK_TOKEN = os.environ['SLACK_BOT_TOKEN'] #본인의 Slack Bot Token 입력
SLACK_CHANNEL = '#test' #메시지를 보낼 Channel명 입력

url = 'https://api.bscscan.com/api?module=account&action=tokentx&contractaddress='+ADDRESS+'&page=1&offset=10000&sort=desc&apikey=' + API_KEY
response = requests.get(url)

transactions = []
for i in response.json()['result']:
    #print(i)
    ts = int(i['timeStamp'])
    temp = {
        'timeStamp': datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
        'from': i['from'],
        'to': i['to'],
        'value': int(i['value'])/1000000000000000000,
        'tokenName': i['tokenName']
    }
    #print(temp)
    transactions.append(temp)

# df = pd.DataFrame(transactions)
# df

def Bscscanbot(slack_messege):  #slack bot massage
    slack_token = SLACK_TOKEN   #slack bot token
    channel = SLACK_CHANNEL     #chnnel for sending massege from slack bot
    message = slack_messege     #message from slack bot 
    client = slack_sdk.WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=message)

chat ="지갑 마지막 transactions :" + transactions[0]  # 보낼 메시지 입력

def message():
    print("Bscscanbot(chat)")
    
Bscscanbot(chat)