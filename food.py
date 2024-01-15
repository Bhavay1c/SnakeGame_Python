# Bhavay Garg
# This class genereates food at random places

from turtle import Turtle
import random


# below is class inheritance
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        """place the food at a random position"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)