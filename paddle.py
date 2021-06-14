from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self. shape("square")
        self.shapesize(stretch_len=5, stretch_wid=None)
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(coordinates)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
