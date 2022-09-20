from constants import *

class Card:
  # cards have suits, ranks and values
  def __init__(self,suit,rank):
    self.suit  = suit
    self.rank  = rank
    self.value = values[rank]

  # return a string identifying a card    
  def __str__(self):
    return self.rank + ' of ' + self.suit