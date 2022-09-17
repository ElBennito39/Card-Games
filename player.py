from functools import reduce

class Player:
  def __init__(self,name):
    self.name = name
    # A new player has no cards
    self.all_cards = [] 
    # A new player has no purse
    self.purse = 0

  def __str__(self):
    # FIXME: This doesn't display strings yet, just object location in memory
    return "Player has the following hand: {} .".format(self.all_cards)

  def add_cards(self,new_cards):
    # extend lists of cards
      if type(new_cards) == type([]):
          self.all_cards.extend(new_cards)
      #or append a single card
      else:
          self.all_cards.append(new_cards)
  
  def hand_total(self):
    #get an integer value for a hand
    def add_values(x, card):
      # printbb(card.value)
      # printbb(x)
      return card.value + x
    return reduce(add_values , self.all_cards, 0) 
    