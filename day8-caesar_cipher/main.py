import math
# def greet(something):
#   print("Hello")
#   print("Hello")
#   print("Hello")

# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")

# greet_with_name('Alex')

#function with more than 1 input

def greet_with_name_and_location(name, location):
  print(f"Hello my name is {name} and I am from {location}")

greet_with_name_and_location("Alex", "New York")

#keyword arguments
def my_function(a,b,c):
  print(a,b,c)

my_function(c = 2, b = 3, a = 1) #order does not matter when you use keywords


#paint area calculator
def paint_calc(height, width, cover):
  can_number = math.ceil((height * width) / cover)
  print(can_number)

test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)

#prime number checker
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number")

n = int(input("Check this number:"))
prime_checker(number = n)