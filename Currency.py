from abc import ABC, abstractmethod

class currency(ABC) :

  @abstractmethod
  def buy(self, exchange, value):
    pass
    
  def sell(self, exchange, value):
    pass
    
  def get_value(self, exchange):
    pass
    
class exchange(ABC) :
    
    @abstractmethod
    def buy(coin, amount):
        pass
    
    @abstractmethod
    def sell(coin, amount):
        pass
    
    @abstractmethod
    def trade(coin1, coin2, amount):
        pass
    
    @abstractmethod
    def checkCoinValue(coin):
        pass
