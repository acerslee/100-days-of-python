#turtle package is giving me issues...

from turtle import Turtle, Screen, colormode
import random

timmy_the_turtle = Turtle()
tim = Turtle()
# timmy_the_turtle.shape("turtle")

timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")
colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r,g,b)



#difference between tuple and array is in tuples you cannot change the values within
my_tuple = (1, 3, 8)
my_tuple[2] #returns 8

for _ in range(200):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(directions))

#drawing diffeent shapes
def draw_shapes(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for shape_side_n in range (3,11):
  tim.color(random_color())
  draw_shapes(shape_side_n)


#drawing a spirograph

def draw_spirograph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)

draw_spirograph(5)

# print(tim.heading()
screen = tim.Screen()
screen.exitonclick()

