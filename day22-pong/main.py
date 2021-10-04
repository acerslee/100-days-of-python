# create the screen
# create and move a paddle
# create another paddle
# create the ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Welcome to the pong game")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# screen.onkey(ball.reset_ball, "space")

is_game_on = True

while is_game_on:
    time.sleep(0.04)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.add_score("left")
    elif ball.xcor() < -380:
        ball.reset_ball()
        score.add_score("right")

    if score.l_score == 7 or score.r_score == 7:
        score.game_over()
        is_game_on = False

screen.exitonclick()