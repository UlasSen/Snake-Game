from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.color("pink")
    
    def new_location(self):
        random_X=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_X,random_y)
