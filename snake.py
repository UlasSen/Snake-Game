from turtle import Turtle,Screen
import time

screen=Screen()
ecem_turtle=Turtle()

STARTING_POSITION =[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0


game_is_on_=True
class Snake:
    
    def __init__(self):
        self.bros=[]
        self.Crate_Snake()
        self.snake_head = self.bros[0]

    def Crate_Snake(self):
        for position in STARTING_POSITION:
            self.add_bros(position)


    def add_bros(self, position):
        ecem_turtle=Turtle(shape="square")
        ecem_turtle.color("White")
        ecem_turtle.penup()
        ecem_turtle.goto(position)
        self.bros.append(ecem_turtle)


    def extend(self):
        self.add_bros(self.bros[-1].position())


    def reset(self):
        for bro in self.bros:
            bro.goto(1000,1000)
        self.bros.clear()
        self.Crate_Snake()
        self.snake_head = self.bros[0]
        

    def Snake_move(self):
        for bro_nums in range(len(self.bros)-1, 0, -1):
            new_x=self.bros[bro_nums-1].xcor()
            new_y=self.bros[bro_nums-1].ycor()
            self.bros[bro_nums].goto(new_x, new_y)
        self.snake_head.forward(MOVE)
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
