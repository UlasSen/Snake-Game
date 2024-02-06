from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.score=0
        self.high_score=0
        self.setposition(0,260)
        self.new_scoreboard()
        self.clear()
    

    

    def new_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align="center",font=("Arial", 15, "normal"))


    def increase_Scoreboard(self):
        
        self.score+=1
        self.new_scoreboard()
        
    
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.new_scoreboard()