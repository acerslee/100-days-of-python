from data import MENU, resources
cash = 20

def dispense_drink(drink, resource_ingredients):
  global cash
  ingredients = MENU[drink]['ingredients']
  drink_cost = MENU[drink]['cost']

  check_resources = True

  #check if there's enough resources
  for item in ingredients:
    if ingredients[item] > resource_ingredients[item]:
      print("Sorry you don't have enough resources")
      check_resources = False
      break
    else:
      resource_ingredients[item] -= ingredients[item]

  #check if there's enough cash
  if check_resources == True:
    if drink_cost < cash:
      cash -= drink_cost
      print(f"Kachunk, here is your {drink}!")
    else:
      print("Sorry, you don't have enough cash")
      return


def coffee_machine():
  machine_on = True

  while machine_on:
    drink_decision = input("What would you like? (espresso/latte/cappuccino): ")

    #to turn off the coffee machine
    if drink_decision == "off":
      print("Machine powering down...")
      machine_on = False

    #to see list of current resources
    if drink_decision == "report":
      message = (
        "Current resources\n"
        f"Water: {resources['water']}\n"
        f"Milk: {resources['milk']}\n"
        f"Coffee: {resources['coffee']}"
      )
      print(message)

    #to start transaction
    if drink_decision == "espresso" or drink_decision == "latte" or drink_decision == "cappuccino":
      dispense_drink(drink_decision, resources)


coffee_machine()