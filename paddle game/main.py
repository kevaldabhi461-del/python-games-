from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scorebord import Score
import time
screen=Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball = Ball()
score=Score()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor()>275 or ball.ycor()<-275:
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.pad_bounce()

    if ball.xcor()>370 :
        ball.reset()
        score.r_point()
    if ball.xcor()<-370:
        ball.reset()
        score.l_point()







screen.exitonclick()