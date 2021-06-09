#Mercenne Twister
import random
import my_module

# random_integer = random.randint(1,10)
# # print(random_integer)

# # print(my_module.pi)

# #prints random number between 0.000000 - 0.9999999
# random_float = random.random()
# print(random_float * 5)

# love_score = random.randint(1, 100)
# print (f"Your love score is {love_score}")

# #heads or tails game
# coin_flip = random.randint(0,1)
# print(coin_flip)
# if coin_flip == 1:
#    print("You got heads!")
# else:
#    print("You got tails!")


# #lists
# states = ["Alaska", "New York", "California", "Missouri"]

# states[2] = "Wisconsin"
# print(states)
# #you can declare negative indices. -1 will start at the end of the array, and work its way back
# print(states[-1])

# #similar to JS's push, use append to add an item at the end of the array
# states.append("New Mexico")
# # you can also use extend to add multiple items from the end of the array
# states.extend(["Pennsylvania", "Maine"])
# print(states)

# #credit card roulette. pick a random name from the array without using the .choice method
# names_string = input("Give me a list of everyone's names, separated by a comma")
# names = names_string.split(", ")
# random_select = random.randint(0, len(names) - 1)
# print(names[random_select] +  " has been selected to pay!")

# Nested lists
# fruits = ["Strawberry", "Watermelon", "Grapes"]
# vegetables = ["Spinach", "Lettuce", "Tomato"]
# food = [fruits, vegetables]
# print(food[1][1]) #returns lettuce


# #treasure map
# row1 = ["","",""]
# row2 = ["","",""]
# row3 = ["","",""]
# map = [row1,row2,row3]

# position = input("where do you want to put the treasure?")
# horizontal = int(position[0])
# vertical = int(position[1])
# map[horizontal - 1][vertical - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

#rock-paper-scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
my_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))
computer_choice = random.randint(0, len(choices) - 1)
if my_choice > 2 or my_choice < 0:
  print("Invalid number")
else:
  print(f"You choose {choices[my_choice]}")
  print(f"Computer chooses {choices[computer_choice]}")
  if my_choice == 0 and computer_choice == 1:
    print("Computer wins with paper")
  elif my_choice == 0 and computer_choice == 2:
    print("You win with rock")
  elif my_choice == 1 and computer_choice == 0:
    print("You win with paper")
  elif my_choice == 1 and computer_choice == 2:
    print("Computer wins with scissors")
  elif my_choice == 2 and computer_choice == 0:
    print("Computer wins with rock")
  elif my_choice == 2 and computer_choice == 1:
    print("You win with scissors")
  else:
    print("Its a draw~")