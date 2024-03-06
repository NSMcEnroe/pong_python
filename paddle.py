from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(5, 1)
        self.color("white")
        self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

