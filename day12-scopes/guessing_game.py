import random
from art import logo
attempts = 0

def guessing_game():
  global attempts
  print(logo)
  print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  beat_game = False

  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  random_number = random.randint(1, 100)

  print(f"You have {attempts} attempts left")
  while attempts > 0 and beat_game == False:
    try:
      guess = int(input("What is your guess?: "))
      if guess not in range(1, 101):
        print("Please enter a number between 1 - 100")
      else:
        if guess > random_number:
          attempts -= 1
          print(f"Your guess was too high. Please try again. You have {attempts} attempts left")
        elif guess < random_number:
          attempts -= 1
          print(f"Your guess was too low. Please try again. You have {attempts} attempts left")
        else:
          print("YES! You've guessed correctly. Nice job!")
          beat_game = True
    except ValueError:
      print("please type in an integer between 1-100")

  if beat_game == False and attempts == 0:
    print ("You Lose")

  try_again = input("Do you want to try again? Type 'y' for yes, or 'n' for no: ")
  if try_again == 'y':
    guessing_game()
  elif try_again == 'n':
    print("Goodbye. Thanks for playing~")


guessing_game()