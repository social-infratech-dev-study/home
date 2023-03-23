import slack_sdk
import os

SLACK_TOKEN = os.environ["BB_SLACK_BOT_TOKEN"]
SLACK_CHANNEL = '#10min-bot' #메시지를 보낼 Channel명 입력

channel = SLACK_CHANNEL     #chnnel for sending massege from slack bot
message = """
  하이 ~!
"""   
client = slack_sdk.WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel=channel, text=message)
