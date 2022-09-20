from logging.handlers import BaseRotatingHandler
from utils import *
from player import Player
from deck import Deck

class Game:
  def __init__(self, name, ante):
    self.name = name
    self.ante = ante

  def __str__(self):
    return "{} is the game.\n".format(self.name)

  
  
  def ask_bet(self,the_pot):
    betting = input("Do you want to bet? Y or N  ")

    if betting.upper() == "Y":
      betting = True
    elif betting.upper() == "N":
      betting = False
    else:
      self.ask_bet(the_pot)

    while betting == True:
      #add the bet to the pot
      the_pot = the_pot + int(input("How much would you like to bet?  "))
      #display the pot
      print("The pot is now {}".format(the_pot))
      #reset the betting value to user decision
      betting = False
          


  def blackjack(self):

    #create Dealer and the User playing the game
    dealer = Player("Dealer")
    user = Player(input("Your name is:  \n"))
    printbb("\n")

    #introduce the game
    printbb(self)
    printbb("The ante is {}".format(self.ante))
    printbb("\n")

    # starting chip purcahse
    user.purse = int(input("Your starting chip count is:  "))
    printbb("\n")
    printbb("You have {} \n".format(user.purse))

    #lets play a round 
    current_round = True
    

    while current_round:
      # clear the console output
      printbb("\n")
      printbb("Let's Play a Hand of Black Jack", False)
      printbb("\n")
      printbb("The ante is {}".format(self.ante))
      printbb("\n")

      # shuffle the deck
      new_deck = Deck()
      the_pot = self.ante

      # when player reaches zero chips the game is over
      if user.purse <= 0:
        game_on = False
        printbb("\n \n {} has no more chips, the game is over...".format(user.name))
        break

      # empty the hands
      dealer.all_cards = []
      user.all_cards = []

      # deal starting hands.
      # Dealer receives one card face up
      dealer.add_cards(new_deck.deal_one())
      print("{} has been dealt to the Dealer.\n".format(dealer.all_cards[0]))

      # User receives two cards.
      user.add_cards(new_deck.deal_one())
      user.add_cards(new_deck.deal_one())
      printbb("You have been dealt the {}, and the {} \n".format(user.all_cards[0], user.all_cards[1]))

      # display the hand values
      printbb("Dealer has {} and you have {}".format(dealer.hand_total(), user.hand_total()))

      #ask for bet

      self.ask_bet(the_pot)

     # Do you want to hit?
      hit_me = input("Do you want to hit? Y or N  ")
      if hit_me.upper() != "Y" and hit_me.upper() != "N":
        hit_me = input("Do you want to hit? Y or N  ")
      else: 
        while hit_me.upper() == "Y":
          user.add_cards(new_deck.deal_one())
          printbb("You now have the hand: {}".format(user.all_cards))
          printbb("Your hand now has a total of {}".format(user.hand_total()))
          hit_me = input("Do you want to hit? Y or N  ")

        while hit_me.upper() == "N":
          #the player stands
          printbb("{} stands.".format(user.name))
          printbb("Your hand has a total of {}".format(user.hand_total()))
          break
    
      
      #check for user bust   
      if user.hand_total() > 21:
        printbb("Bust, you lose the hand")
        # player loses the pot
        user.purse = user.purse - the_pot
        # the round is over
        current_round = False

      else:
        # Do the dealers hand.. if not a bust by user
        # deal the Dealer's second card
        dealer.add_cards(new_deck.deal_one())

      # dealer has to hit too
        while dealer.hand_total() <= 16:
          printbb("The Dealer has {} \n".format(
            dealer.hand_total()))
          printbb("The Dealer has less than 17 and hits.")
          dealer.add_cards(new_deck.deal_one())

      # check if dealer busts   
        if dealer.hand_total() > 21:
          print("The Dealer busts, {} wins the hand and collects {}".format(user.name, the_pot))
          # the player wins the pot
          user.purse = user.purse + the_pot
          # the round is over
          current_round = False

        else:
            # say what the dealer ends up with after hitting
          printbb("The dealer's hand has a total of {}".format(dealer.hand_total()))
            # the dealer loses
          if user.hand_total() > dealer.hand_total():
            # player wins, add pot to player's purse
            printbb("{} wins the hand and the {} pot".format(user.name, the_pot))
            user.purse = user.purse + the_pot
            current_round = False

          elif dealer.hand_total() > user.hand_total():
            # player loses, subtract pot from player's purse
            printbb("{} loses the hand".format(user.name))
            user.purse = user.purse - the_pot
            current_round = False
          
          else:
            # it is a draw and player gets his bet back, but not the ante
            printbb("{} and the Dealer draw the hand, only the ante is not recovered".format(user.name))
            user.purse = user.purse - self.ante
            current_round = False
        










##############
      # while hit_me:
      #   hit = input("Do you want to hit? Y or N  ")
      #   if hit == "Y":
      #     user.add_cards(new_deck.deal_one())
      #     printbb("You now have the hand: {}".format(
      #       user.all_cards))
      #     printbb("Your hand now has a total of {}".format(
      #       user.hand_total()))

      #     #check to see if there is a bust
      #     if user.hand_total() > 21:
      #       printbb("Bust, you lose the hand")
      #       # player loses the pot
      #       user.purse = user.purse - the_pot
      #       # no more hitting
      #       hit_me = False
      #       # the round is over
      #       current_round = False
      #       break

      #   elif hit == "N":
      #     # the player stands
      #     printbb("{} stands.".format(user.name))
      #     printbb("Your hand has a total of {}".format(user.hand_total()))
      #     hit_me = False
      #     break

      #   else: 
      #     hit = input("Do you want to hit? Y or N  ")
          

      # # deal the Dealer's second card
      # dealer.add_cards(new_deck.deal_one())

      # # dealer has to hit too
      # while dealer.hand_total() <= 16:
      #   printbb("The Dealer has {} \n".format(
      #     dealer.hand_total()))
      #   printbb("The Dealer has less than 17 and hits.")
      #   dealer.add_cards(new_deck.deal_one())

      # # check to see if dealer busts
      # if dealer.hand_total() > 21:
      #   print("The Dealer busts, {} wins the hand and collects {}".format(user, the_pot))
      #   # the player wins the pot
      #   user.purse = user.purse + the_pot
      #   # the round is over
      #   current_round = False
      

      # # no more hitting
      # hit_me = False
        

    


