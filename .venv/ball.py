from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(45)
        self.move()

    def move(self):
        self.forward(20)

    def collision(self):
        new_angle = self.heading() - 90
        self.setheading(new_angle)

    def reset(self):
        new_angle = self.heading() + 180
        self.goto(0,0)
        self.setheading(new_angle)