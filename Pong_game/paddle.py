from turtle import *
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.len = 1
        self.wid = 5
        self.shaper = "square"
        self.speed("fastest")
        self.shape(self.shaper)
        self.color("white")
        self.shapesize(stretch_wid=self.wid, stretch_len=self.len)
        self.penup()
        self.goto(self.x,self.y)

  

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
        self.speed("fastest")

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
        self.speed("fastest")

    # def go_left(self):
    #     new_x = self.xcor()-20
    #     self.goto(new_x,self.ycor())

    # def go_right(self):
    #     new_x = self.xcor()+20
    #     self.goto(new_x,self.ycor())

            