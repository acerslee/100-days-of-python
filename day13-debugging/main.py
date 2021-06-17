#describe the problem
#reproduce the bug

from random import randint
# dice_img = [1,2,3,4,5,6]
# #since we know that line 7 is causing the issue, we can test one number at a time to figure out which number is throwing the consistent bug. Once figured out, we fix the line below.
# dice_number = randint(0,5)
# print(dice_img[dice_number])

# #play computer
# year = int(input("What's your year of birth?: "))
# if year > 1980 and year <= 1994:
#   print("You are a millenial")
# elif year > 1994:
#   print("You are a Gen Z-er")


# #fix errors and watch for red underlines
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")


# #print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)


#using a debugger
#add a breakpoint in your code and run the debugging tool.
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])