from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
  options = menu_list.get_items()
  choice = input(f"What would you like? ({options})")
  if choice == "off":
    print("Goodbye")
    is_on = False
  elif choice == "report":
    print(coffee_maker.report())
    print(money_machine.report())
  else:
    drink = menu_list.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
      print("here is your coffee!")
    else:
      print("Sorry you do not have enough resources")
