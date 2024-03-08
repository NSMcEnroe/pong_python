from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    if ball.xcor() > 320 or ball.xcor() < -320:
        if paddle1.distance(ball) < 50 or paddle2.distance(ball) < 50:
            ball.collision()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.collision()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.reset()

screen.exitonclick()
