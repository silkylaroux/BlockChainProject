import numpy as np
import requests as req
import json
stable_coin = 'USDC'


def get_name():
    return "CoinBase"


# This returns the ask/bid spread of the coin as it relates to the stable coin of this exchange
def get_spread(coin1, coin2=stable_coin):
    spread = {
        'ask': 1,
        'bid': 1,
    }
    if coin1 == stable_coin:
        return spread
    r2 = req.get("https://api.coinbase.com/v2/exchange-rates?currency=" + coin1)
    r = req.get("https://api.coinbase.com/v2/exchange-rates?currency=" + coin2)
    pair = json.loads(r.text)
    # print(pair)
    ask = 1/(float(pair['data']['rates'][coin1]))*0.99
    spread['ask'] = ask
    pair = json.loads(r2.text)
    # print(pair)
    bid = float(pair['data']['rates'][coin2])*1.01
    spread['bid'] = bid
    # print(coin1, spread)
    return spread


# gives the buy/sell price from USD, as opposed to exchange rates
def alternate_spread(coin):
    spread = {}
    r2 = req.get("https://api.coinbase.com/v2/prices/" + coin + "-USD/buy")
    r = req.get("https://api.coinbase.com/v2/prices/" + coin + "-USD/sell")
    pair = json.loads(r.text)
    # print(pair)
    ask = float(pair['data']['amount'])
    spread['ask'] = ask
    pair = json.loads(r2.text)
    # print(pair)
    bid = float(pair['data']['amount'])
    spread['bid'] = bid
    print(coin, spread)
    return spread


def buy(coin1, amount, coin2=stable_coin):
    print("Unimplemented Until API Key is given", coin1, amount, coin2)
    # This will be a call to the api to trade


def sell(coin1, amount, coin2=stable_coin):
    print("Unimplemented Until API Key is given", coin1, amount, coin2)
