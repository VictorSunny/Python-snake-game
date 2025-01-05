from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shapesize(0.5)
        self.shape("circle")
        self.appear()

    def appear(self):
        ranx = randint(-280, 280)
        rany = randint(-280, 280)
        self.setposition(ranx, rany)