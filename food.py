from turtle import Turtle
import random
COLORS = ("blue", "red", "orange", "pink", "purple", "green")


class SnekFood(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.got_eaten()

    def got_eaten(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 350)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
