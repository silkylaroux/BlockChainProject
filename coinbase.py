import numpy as np
import requests as req
import json
stable_coin = 'USD'


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
    r = req.get("https://api.coinbase.com/v2/prices/" + coin1 + "-" + coin2 +"/buy")
    r2 = req.get("https://api.coinbase.com/v2/prices/" + coin1 + "-" + coin2 +"/sell")
    pair = json.loads(r.text)
    #print(pair)
    ask = pair['data']['amount']
    spread['ask'] = ask
    pair = json.loads(r2.text)
    #print(pair)
    bid = pair['data']['amount']
    spread['bid'] = bid
    #print(coin1, spread)
    return spread


def buy(coin1, amount,coin2=stable_coin):
    print("Unimplemented Until API Key is given", coin1, amount, coin2)
    # This will be a call to the api to trade


def sell(coin1, amount, coin2=stable_coin):
    print("Unimplemented Until API Key is given", coin1, amount, coin2)
