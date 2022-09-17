from utils import *
from player import Player
from deck import Deck

class Game:
  def __init__(self, name, ante):
    self.name = name
    self.ante = ante

  def __str__(self):
    return " {} is the game.".format(self.name)

  def blackjack(self):
    # create dealer and player(s)
    player_one = Player("Dealer")
    player_two = Player(input("Your name is:  "))

    # starting chip purcahse
    player_two.purse = int(input("Your starting chip count is:  "))
    printbb("You have {}".format(player_two.purse))

    # introduce the game
    printbb("\n \n The User has approached the table to gamble. \n \n")

    game_on = False

    # Do you want to play
    start_game = list(
      input("Do you want to play a hand? Y or N  ").lower())

    if start_game[0] == 'y':
      game_on = True

      # alright, lets play then
      while game_on:
        # create the deck
        new_deck = Deck()

        # reinitialize the deck for the game
        printbb("\n \n The deck has been shuffled \n \n")

        # ante
        printbb("The ante is {} \n".format(self.ante))

        # lets gamble!

        current_round = True

        while current_round:
          # clear the console output
          printbb("Let's Play a Hand of Black Jack", False)

          # shuffle the deck
          new_deck = Deck()

          # when player reaches zero chips the game is over
          if player_two.purse <= 0:
            game_on = False
            printbb("\n \n {} has no more chips, the game is over...".format(
              player_two.name))
            break

          # clear hands from players

          player_one.all_cards = []
          player_two.all_cards = []

          # player purse display
          printbb("{} chips: {}".format(
            player_two, player_two.purse))

          # pay ante and plus whatever your wager is (resets pot from last hand)
          the_pot = self.ante + \
            int(input(
              "The ante is {}. How much do you wager:  ".format(self.ante)))

          # deal starting hands.
          # Dealer receives one card face up
          player_one.add_cards(new_deck.deal_one())
          print("{} has been dealt to the Dealer.\n".format(
            player_one.all_cards[0]))

          # User receives two cards.
          player_two.add_cards(new_deck.deal_one())
          player_two.add_cards(new_deck.deal_one())
          printbb("You have been dealt the {}, and the {} \n".format(
            player_two.all_cards[0], player_two.all_cards[1]))

          # display the hand values
          printbb("Dealer has {} and you have {}".format(
            player_one.hand_total(), player_two.hand_total()))

          # does the User want to place a bet
          place_bet = True

          while place_bet:
            if input("Would you like to place another bet? Y or N  ") == "Y":
              the_pot = the_pot + \
                int(input("How much would you like to bet?  "))
              print("The pot is now {}".format(the_pot))
              place_bet = False
              break

            elif input("Would you like to place another bet? Y or N  ") == "N":
              print("The pot is {}".format(the_pot))
              place_bet = False
              break

            else:
              printbb("Answer the question.")

          # Do you want to hit?
          hit_me = True

          while hit_me:
            if input("Do you want to hit? Y or N  ") == "Y":
              player_two.add_cards(new_deck.deal_one())
              printbb("You now have the hand: {}".format(
                player_two.all_cards))
              printbb("Your hand now has a total of {}".format(
                player_two.hand_total()))

              if player_two.hand_total() > 21:
                printbb("Bust, you lose the hand")
                # player loses the pot
                player_two.purse = player_two.purse - the_pot
                # no more hitting
                hit_me = False
                # the round is over
                current_round = False
                break

            elif input("Do you want to hit? Y or N  ") == "N":
              # the player stands
              printbb("{} stands.".format(player_two.name))
              printbb("Your hand has a total of {}".format(player_two.hand_total()))

              # deal the Dealer's second card
              player_one.add_cards(new_deck.deal_one())

              # dealer has to hit too
              while player_one.hand_total() <= 16:
                printbb("The Dealer has {} \n".format(
                  player_one.hand_total()))
                printbb("The Dealer has less than 17 and hits.")
                player_one.add_cards(new_deck.deal_one())

              # check to see if dealer busts
              if player_one.hand_total() > 21:
                print("The Dealer busts, {} wins the hand and collects {}".format(player_two, the_pot))
                # the player wins the pot
                player_two.purse = player_two.purse + the_pot
                # the round is over
                current_round = False
                break

              # no more hitting
              hit_me = False
              break

            else:
              printbb("Answer the question")

          # clear out some text space
          printbb("\n")

          # display the hand values
          printbb("Dealer has {} and you have {}".format(
            player_one.hand_total(), player_two.hand_total()))

          # compare hands that are not busted.
          # the dealer loses
          if player_two.hand_total() > player_one.hand_total():
            # player wins, add pot to player's purse
            printbb("{} wins the hand and the {} pot".format(player_two.name, the_pot))
            player_two.purse = player_two.purse + the_pot
            current_round = False
          elif player_one.hand_total() > player_two.hand_total():
            # player loses, subtract pot from player's purse
            printbb("{} loses the hand".format(player_two.name))
            player_two.purse = player_two.purse - the_pot
            current_round = False
          else:
            # it is a draw and player gets his bet back, but not the ante
            printbb("{} and the Dealer draw the hand, only the ante is not recovered".format(player_two.name))
            player_two.purse = player_two.purse - self.ante
            current_round = False
    else:
      game_on = False
