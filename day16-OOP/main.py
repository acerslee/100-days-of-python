#to use OOP this is in an object = class format
# car = CarBlueprint()

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("orange")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Mew", "Squirtle"])
table.add_column("Type", ["Electric", "Unknown", "Water"])

table.align = 'l'
print(table)