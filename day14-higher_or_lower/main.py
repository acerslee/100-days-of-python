import random
import art
from data import data

high_score = 0
current_score = 0
game_start = True

def clash(guess, choiceA, choiceB):
  global current_score, high_score, game_start
  if guess == 'A':
    if choiceA['follower_count'] > choiceB['follower_count']:
      current_score += 1
      print(f"You're right! Current score: {current_score}")
      return
  elif guess == 'B':
    if choiceB['follower_count'] > choiceA['follower_count']:
      current_score += 1
      print(f"You're right! Current score: {current_score}")
      return
  print(f"Game Over. Your score is {current_score}")
  if current_score > high_score:
    high_score = current_score
  game_start = False

def game():
  global game_start
  print(art.logo)

  random_choice_a = random.choice(data)
  random_choice_b = random.choice(data)

  while game_start:
    print(f"Compare A: {random_choice_a['name']}, a {random_choice_a['description']}, from {random_choice_a['country']}")
    print(art.vs)
    print(f"Compare B: {random_choice_b['name']}, a {random_choice_b['description']}, from {random_choice_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    clash(guess,random_choice_a, random_choice_b)
    random_choice_a = random_choice_b
    random_choice_b = random.choice(data)


  if game_start == False:
    try_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if try_again == 'yes':
      game_start = True
      game()
    else:
      print(f"Thank you for playing. Your high score is {high_score}. Goodbye")

game()