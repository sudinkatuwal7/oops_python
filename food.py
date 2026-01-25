import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=1)         #original(20, 20) but it becomes (10, 10)
        self.refresh()

    def refresh(self):
        a = random.randint(-280, 280)
        b = random.randint(-280, 280)
        self.goto(a,b)
