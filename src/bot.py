from coinapi_rest_v1 import CoinAPIv1
from discord_webhook import DiscordWebhook
from config import *
import datetime, sys

test_key = sys.argv[1]

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()

def get_info(crypto):
    exchange_rate = api.exchange_rates_get_specific_rate(crypto, 'USD')

    return exchange_rate

def discord(message):
    webhook = DiscordWebhook(
        url=webhook_uri, 
        content=message)
    webhook.execute()

def notify(message):
    discord(message)

if __name__ == "__main__":
    cryptos = ['BTC']
    infos = []

    for crypto in cryptos:
        infos.append(get_info(crypto))

    for info in infos:
        msg = '{} price ({}): ${:.2f}'.format(info['asset_id_base'], info['asset_id_quote'], info['rate'])
        notify(msg)