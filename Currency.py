from abc import ABC, abstractmethod

class currency(ABC) :

  @abstractmethod
  def buy(self, exchange, value):
    pass
    
  def sell(self, exchange, value):
    pass
    
  def get_value(self, exchange):
    pass
    
#class exchange(ABC) :
#TODO
