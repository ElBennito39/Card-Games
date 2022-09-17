import random

from card import Card   # needed to create new Cards for Deck
from constants import * # import card definitions for suits/rank

class Deck:
  def __init__(self):
    self.all_cards = [] 
    for suit in suits:
      for rank in ranks:
        self.all_cards.append(Card(suit,rank))
    self.shuffle()  
              
  def shuffle(self):
    # Note this doesn't return anything
    random.shuffle(self.all_cards)
      
  def deal_one(self):
    # Note we remove one card from self.all_cards
    return self.all_cards.pop()

  def deal_cards(self, player):
    # Deal one card from self.all_cards to Player
    new_cards = self.deal_one
    player.add_cards(new_cards)
