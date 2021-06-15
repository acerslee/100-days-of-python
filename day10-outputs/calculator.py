from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculation():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  symbol = input("Pick an operations from the line above: ")
  num2 = float(input("What's the second number?: "))

  calculation_function = operations[symbol]
  answer = calculation_function(num1, num2)

  print(f"{num1} {symbol} {num2} = {answer}")
  continue_calculation = True

  while continue_calculation:
    proceed = input("Do you want to continue calculation? Hit y to continue or n to stop: ")
    if proceed == "n":
      continue_calculation = False
      calculation()
    elif proceed == "y":
      previous_answer = answer
      symbol = input("Pick an operations: ")
      num3 = float(input("What's the next number?: "))
      calculation_function = operations[symbol]
      answer = calculation_function(previous_answer, num3)

      print(f"{previous_answer} {symbol} {num3} = {answer}")

    else:
      print("That is not a valid choice")

calculation()