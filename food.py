from turtle import Turtle
import random


class SnekFood(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.got_eaten()

    def got_eaten(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 350)
        self.goto(random_x, random_y)
