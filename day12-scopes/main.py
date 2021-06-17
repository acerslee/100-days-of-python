#there is no such thing as a block scope in python
#however there is local/global scopes in python

#modifying global scope

enemies = 1

def increase_enemies():
  #without this line, you cannot modify something that is a global scope
  global enemies
  enemies += 1
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside funciton: {enemies}")

#Global constants
pi = 3.14159
