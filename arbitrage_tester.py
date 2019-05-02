import numpy as np
import shapeshift as ss
import binanceExchange as be
import coinbase as cb
import time
import sys

def get_arbitrage_opportunities():
    opportunities = []
#    highestretun = 0
    for ask in ArbitrageTester.exchanges:
        for bid in ArbitrageTester.exchanges:
            for coin in ArbitrageTester.coins:
                profit = get_profit(ask, bid, coin)
#                if profit > highestretun:
#                    highestretun = profit
                if is_profitable(profit):
                    opportunities.append({
                        'Coin': coin,
                        'Profit': profit,
                        'Ask_Exchange': ask.get_name(),
                        'Bid_Exchange': bid.get_name(),
                        'Ask_Spread': get_spread(ask, coin),
                        'Bid': get_spread(bid, coin),
                    })
                    print(opportunities[len(opportunities) - 1])
#    if len(opportunities) == 0:
#        print("Highest Return: ", highestretun)
    return opportunities


# Call This Regularly, Or Create Separate Thread For It Alone
def update_data():
    for exchange in ArbitrageTester.exchanges:
        for coin in ArbitrageTester.coins:
            spread = exchange.get_spread(coin)  # All Exchanges Need To Implement get_spread, buy, and sell Methods
            print(exchange.get_name(), coin, spread)
            ArbitrageTester.ask_data[ArbitrageTester.exchanges[exchange]][ArbitrageTester.coins[coin]] = spread['ask']
            ArbitrageTester.bid_data[ArbitrageTester.exchanges[exchange]][ArbitrageTester.coins[coin]] = spread['bid']
    print("Prices Updated")


def get_spread(exchange, coin):
    spread = {
        # Spread Always Is Confusing To Me So Here Is A Note For Help:
        # Ask Is The Price At Which An Exchange Will Buy A Currency From You
        # Bid Is The Cost Per Currency If You Wanted To Buy Some From An Exchange
        # When This Method Is Referenced It Returns The
        # Spread That An Exchange Offers In Terms Of That Exchanges Stable Coin
        # TLDR: ask = sell, bid = buy
        'ask': ArbitrageTester.ask_data[ArbitrageTester.exchanges[exchange]][ArbitrageTester.coins[coin]],
        'bid': ArbitrageTester.bid_data[ArbitrageTester.exchanges[exchange]][ArbitrageTester.coins[coin]]
    }
    return spread


# This Retruns The Profit Ratio That Exists From Buying A Currency On Exchange1 And Selling It On Exchange B
def get_profit(ask_exchange, bid_exchange, coin):
    ask_exchange_spread = get_spread(ask_exchange, coin)
    bid_exchange_spread = get_spread(bid_exchange, coin)
    # print('Exchange spreads', ask_exchange_spread, bid_exchange_spread)
    return calculate_profit(ask_exchange_spread['bid'], bid_exchange_spread['ask'])


def is_profitable(profit):
    padding = .000  # For Now Lets Just Find Any Profit
    return profit > 1 + padding  # Adjust This Number To Add Padding For Mining/Exchange Fees


def calculate_profit(ask, bid):   # This Takes No Fees Into Account
    result = (ask-bid)/bid
    result = 1 - result
    # print('ROE From Spreads: ', result)
    return result


class ArbitrageTester:
    coins = {
        'ETH':  0,
        'XRP':  1,
        'BTC':  2,
    }
    exchanges = {
        ss: 0,
        cb: 1,
        be: 2,
    }
    filename = ""
    ask_data = np.zeros((len(exchanges), len(coins)))
    bid_data = np.zeros((len(exchanges), len(coins)))
    running = True

    @staticmethod
    def run():
        last_updated = 0
        while True:
            if time.time() - last_updated > 60 * 10:
                update_data()
                ops = get_arbitrage_opportunities()
                last_updated = time.time()
                if len(ops) > 0:
                    file = open(ArbitrageTester.filename, 'a')
                    for op in ops:
                        file.write(str(op)+ '\n')

    def __init__(self, file):
        ArbitrageTester.filename = file


if __name__ == "__main__":
    file = sys.argv[1]
    at = ArbitrageTester(file)
    at.run()
    # eth = get_spread(ss, 'ETH')
    # doge = get_spread(ss, 'DOGE')
    # print(eth, doge)
    # prof = get_profit(ss, ss, 'ETH')
    # prof = calculate_profit(1.1910, 1.1970515)
    # print(prof)
    # opport = get_arbitrage_opportunities()
    # print(opport)
    # print(5000000*prof)
    # print(get_spread(ss, 'ETH'))
    # print(ArbitrageTester.ask_data)
