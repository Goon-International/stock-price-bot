from discord_webhook import DiscordWebhook
from config import *
import sys, requests, json
from datetime import date, timedelta

def get_info(stocks, api_key):
    infos = []
    
    for stock in stocks:
        yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        r = requests.get(f'https://api.polygon.io/v1/open-close/{stock}/{yesterday}?apiKey={api_key}')
        infos.append(json.loads(r.text))

    return infos

def discord(message):
    webhook = DiscordWebhook(
        url=webhook_uri, 
        content=message)
    webhook.execute()

def notify(message):
    discord(message)

if __name__ == "__main__":
    api_key = sys.argv[1]
    stocks = ['PTON', 'PLTR', 'PUBM', 'UPST']
    infos = infos = get_info(stocks, api_key)

    msg = 'Today\'s Date: {}\nYesterday\'s stock prices:\n\n'.format(date.today().strftime('%Y-%m-%d'))
    for i in range(len(infos)):
        msg += '{} ({})\nOpen: ${:.2f}\nClose: ${:.2f}\n\n'.format(
            stocks[i],
            infos[i]['from'],
            infos[i]['open'], 
            infos[i]['close']
        )

    notify(msg.strip())
    