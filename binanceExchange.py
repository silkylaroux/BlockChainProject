from binance.enums import *
from binance.exceptions import BinanceAPIException
import pandas as pd
import Currency as curr
from datetime import datetime
from binance.client import Client

def get_name():
    return "Binance"


class binanceExchange(curr.exchange):

    api_key = "mLNccbkPLVx0Y2SgxyjK1UUNDHR5Vkn4NEVD7fPk8IXk5g4o9S4UMURlVNuXoJMC"
    api_secret = "idLU83recXRYrvxGOf5O5H44mG80PkEJCj2loiyd1BYOaisU7KreT16GTEHXt8x1"
    client = Client(api_key, api_secret)
    #prices = client.get_all_tickers()
    prices = ''
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
                order = client.create_test_order(
                    symbol=coin,
                    side=Client.SIDE_BUY,
                    type=Client.ORDER_TYPE_MARKET,
                    quantity=amount)
            except BinanceAPIException as e:
                print(e)
            else:
                print("Success")
                
    # This returns the ask/bid spread of the coin as it relates to the stable coin of this exchange
    def get_spread(self, coin1, coin2='USDT'):
        spread = {
            'ask': 1,
            'bid': 1,
        }
        
        coinValTemp1 = self.checkCoinValue(coin1+coin2)
        coinValTemp2 = self.checkCoinValue(coin2+coin1)
        
        if (coinValTemp1 != {}):
            spread['ask'] = float(coinValTemp1['price'])
            bid = float(coinValTemp1['price'])
            spread['bid'] = bid
        elif (coinValTemp2 != {}):
            ask = float(coinValTemp2['price'])
            spread['ask'] = 1/ask
            spread['bid'] = 1/float(coinValTemp2['price'])
            
        return spread
        
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
            return self.client.get_symbol_ticker(symbol=coin)
        return {}    
   
