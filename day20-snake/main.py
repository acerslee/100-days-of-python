from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
# create keyboard functions, and bind the appropriate methods from the snake class
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.randomize()
        score.add_score()
        snake.extend_snake()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.reset()
            snake.reset()

screen.exitonclick()