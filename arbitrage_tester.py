import numpy as np
import shapeshift as ss


# Call This Regularly, Or Create Separate Thread For It Alone
def update_data():
    for exchange in ArbitrageTester.exchanges:
        for coin in ArbitrageTester.coins:
            spread = exchange.get_spread(coin)  # All Exchanges Need To Implement get_spread, buy, and sell Methods
            print(coin, spread)
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
# This Assumes That All Costs (Mining/Exchange) Add Up To 25% Of The Initial Investment
def get_profit(ask_exchange, bid_exchange, coin):
    ask_exchange_spread = get_spread(ask_exchange, coin)
    bid_exchange_spread = get_spread(bid_exchange, coin)
    print('Exchange spreads', ask_exchange_spread, bid_exchange_spread)
    return calculate_profit(ask_exchange_spread['bid'], bid_exchange_spread['ask'])


def is_profitable(profit):
    padding = .004
    return profit > 1 + padding  # Adjust This Number To Add Padding For Mining/Exchange Fees


def calculate_profit(ask, bid):   # This Takes No Fees Into Account
    result = ask * 1/bid  # Can Also Do (ask - bid)/bid
    result = 2 - result   # If you do that change this line to 1 - results
    print('ROE From Spreads: ', result)
    return result


class ArbitrageTester:
    coins = {
        'DAI':  0,
        'ETH':  1,
        'DOGE': 2,
        'XRP':  3,
        'BTC':  4,
    }
    exchanges = {
        ss: 0,
    }
    ask_data = np.zeros((len(exchanges), len(coins)))
    bid_data = np.zeros((len(exchanges), len(coins)))
    running = True

    def __init__(self, ):
        update_data()


if __name__ == "__main__":
    at = ArbitrageTester()
    eth = get_spread(ss, 'ETH')
    doge = get_spread(ss, 'DOGE')
    # print(eth, doge)
    # prof = get_profit(ss, ss, 'ETH')
    prof = calculate_profit(1.1910, 1.1970515)
    # print(5000000*prof)
    # print(get_spread(ss, 'ETH'))
    # print(ArbitrageTester.ask_data)
