from turtle import *

class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.x =x
        self.y = y
        # self.write(f"Score: {self.score}",align="center", font="Arial,24,normal")
        self.color("white")
        self.penup()
        self.goto(x,y)
        self.hideturtle()

    def update_scoreboard_r(self):
        self.write(f"{self.score_r}",align="center", font="Arial,36,normal")

    def update_scoreboard_l(self):
        self.write(f"{self.score_l}",align="center", font="Arial,36,normal")

 
    def increase_score_l(self):
        self.score_l+=1
        self.clear()
        # self.write(f"{self.score_l}",align="center", font="Arial,30,normal")

    def increase_score_r(self):
        self.score_r+=1
        self.clear()
        # self.write(f"{self.score_r}",align="center", font="Arial,30,normal")

    # def end_game(self):
    #     if self.score_l == 10:
    #         self.write("Player 1 Wins!", align="center", font=("Courier", 16,"normal"))
    #     if self.score_r==10:
    #         self.write("Player 2 Wins!", align="center", font=("Courier", 16,"normal"))
        
             

