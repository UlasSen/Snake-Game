from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import ScoreBoard



screen=Screen()

import time

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
scoreboard=ScoreBoard()
ScoreBoard()
snake=Snake()
food=Food()
food.new_location()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on_=True
while game_is_on_:
    screen.update()
    time.sleep(0.1)
    snake.Snake_move()

    if snake.snake_head.distance(food) < 20:
        food.new_location()
        snake.extend()
        scoreboard.increase_Scoreboard()

    cx, cy =snake.snake_head.position()

    if cx>290 or cx<-290 or cy>290 or cy<-290:
        scoreboard.reset()
        snake.reset()
        
    
    for bro in snake.bros:
        if bro==snake.snake_head:
            pass

        elif snake.snake_head.distance(bro) < 10:
            scoreboard.reset()
            snake.reset()
            














screen.exitonclick()