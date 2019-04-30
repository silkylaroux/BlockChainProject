from binance.enums import *
from binance.exceptions import BinanceAPIException
import pandas as pd
import Currency as curr
from datetime import datetime
from binance.client import Client


class binanceExchange(curr.exchange):
    api_key = "jSPb8feugaZVXgl5BdI22FBO3SgzjmXulU5X8tEYyP8InKCrCzJzzSQVT9zqIL2l"
    api_secret = "dwyfKss4wEaWkCzyPxvEoL4CLg4vdsKxSYHxLslJyEOvDVRhX8UURlj3m2r8XPKQ"
    client = Client(api_key, api_secret)
    prices = client.get_all_tickers()
    cryptos = client.get_products()
    
    #=================================================================
    # DO NOT USE THIS MORE THAN ONCE EVERY 2 MINUTES, WILL GET BANNED!
    #=================================================================
    # Helper method which gets the most recent ticker prices for
    # all the tickers from the API.
    def updatePrices(self):
        self.prices = self.client.get_all_tickers()
        
    # Helper method to see if coin is available from the binance api
    def checkCoinAvailability(self, coinSymbol):
        for x in self.cryptos['data']:
            if x['marketName'] == coinSymbol:
                return True
            if x['symbol'] == coinSymbol:
                return True
        return False

   #TODO
    def buy(self, coin, amount):
        if(self.checkCoinAvailability(coin)):
            try:            
                order = self.client.create_test_order(
                    symbol=coin,
                    side=self.Client.SIDE_BUY,
                    type=self.Client.ORDER_TYPE_MARKET,
                    quantity=amount)
            except BinanceAPIException as e:
                print(e)
            else:
                print("Success")
   
    #TODO            
    def sell(self, coin, amount):
        pass
    
    #TODO
    def trade(self, coin1, coin2, amount):
        pass
    
    # Must put in the coin as COIN + OTHERCOIN
    # Example: checkCoinValue(ETHUSDT)
    def checkCoinValue(self, coin):
        if(self.checkCoinAvailability(coin)):
            for x in self.prices:
                if x['symbol'] == coin:
                    return x['price']
        return None     
   