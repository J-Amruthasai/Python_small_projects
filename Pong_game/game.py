# Pong Game

# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with the paddles
# 7. Detect when paddle misses
# 8. Keep score

import time
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle=Paddle(360,0)
l_paddle=Paddle(-360,0)
ball = Ball()
scoreboard_l = ScoreBoard(300,250)
scoreboard_r = ScoreBoard(-300, 250)

# t_paddle=Paddle(0,250,1,5)


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
# screen.onkey(r_paddle.go_left,"Left")
# screen.onkey(r_paddle.go_right,"Right") 

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
# screen.onkey(l_paddle.go_left,"a")
# screen.onkey(l_paddle.go_right,"d") 


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor()>275 or ball.ycor()<-275:
        ball.bounce_y()
    if (ball.distance(r_paddle)<70 and ball.xcor()>330):
        ball.bounce_x()
        scoreboard_l.increase_score_l()
        scoreboard_l.update_scoreboard_l()
    if  (ball.distance(l_paddle)<70 and ball.xcor()<-330):
        ball.bounce_x()
        scoreboard_r.increase_score_r()
        scoreboard_r.update_scoreboard_r()
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.reset_position()
    # if scoreboard_l.end_game() or scoreboard_r.end_game():
        # game_on = False


screen.exitonclick()



