from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if paddle1.distance(ball) < 50 and ball.xcor() > 320 or paddle2.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
