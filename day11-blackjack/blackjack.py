import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  print(logo)

  player_cards = []
  computer_cards = []
  game_start = True
  isDone = False

  #helper function to initialize the hands
  def initialize_hands():
    if len(player_cards) == 2 and len(computer_cards) == 2:
      print(f"Your cards are {player_cards}. The total is currently {sum(player_cards)}")
      print(f"The computer cards are {computer_cards[1]}")
      return

    random_card = random.choice(cards)
    player_cards.append(random_card)
    random_card = random.choice(cards)
    computer_cards.append(random_card)
    initialize_hands()

  #helper function for when the game ends.
  def end_game():
    new_game = input("Do you want to play another game? Press y to continue, or n to exit: ")
    if new_game == "y":
      blackjack()
    elif new_game == "n":
      print("Thank you for playing")
      quit()
    else:
      print("That is not a valid choice. Please try again")
      end_game()


  initialize_hands()

  while game_start:
    player_choice = input("Do you want to hit or stop? Press y to hit, or n to stop: ")
    print(player_choice)
    if player_choice == "y":
      random_card = random.choice(cards)
      player_cards.append(random_card)
      print(f"Your cards are {player_cards}. The total is currently {sum(player_cards)}")
    elif player_choice == "n":
      print("Holding...")
      isDone = True
    else:
      print("That is not a valid choice. Please try again")
      continue

    #computer (dealer) must pick up if the total value of its cards is less than 17.
    while sum(computer_cards) < 17:
      random_card = random.choice(cards)
      computer_cards.append(random_card)

    #conditional if anyone goes over 21
    if sum(player_cards) > 21 or sum(computer_cards) > 21:
      #determine if each player has an "11"
      if 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
        print (f"The new total is now {sum(player_cards)}")
      if 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)

      if sum(player_cards) > 21:
        print("You lose. You busted")
        end_game()
      elif sum(computer_cards) > 21:
        print ("You win. Computer busted")
        end_game()

    #conditional if the player is done picking up and computer has cards with a value of more than 16.
    if isDone and sum(computer_cards) > 16:
      if sum(player_cards) > sum(computer_cards) and sum(player_cards) < 22:
        print(f"You have {sum(player_cards)} and computer has {sum(computer_cards)}. You win the flop!")
        end_game()
      elif sum(player_cards) < sum(computer_cards) and sum(computer_cards) < 22:
        print(f"You have {sum(player_cards)} and computer has {sum(computer_cards)}. Computer wins the flop")
        end_game()
      elif sum(player_cards) == sum(computer_cards):
        print(f"You have {sum(player_cards)} and computer has {sum(computer_cards)}. Game ended in a draw!")
        end_game()

blackjack()