from scorebord import Score
from turtle import Screen
from snack import Snack
from  food import Food
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snack game")
screen.tracer(0)
screen.listen()


snack=Snack()

food=Food()
score=Score()
screen.onkey(snack.up,"w")
screen.onkey(snack.left,"a")
screen.onkey(snack.down,"s")
screen.onkey(snack.right,"d")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.distance(food)<15:
        food.refresh()
        snack.extand()
        score.increase_score()

    if snack.head.xcor()>280 or snack.head.xcor()<-280 or snack.head.ycor()>280 or snack.head.xcor()>280 or snack.head.ycor()<-280:
        score.reset()
        snack.reset()

    for seg in snack.snacks[1:]:
        if seg==snack.head:
            pass
        elif snack.head.distance(seg)<10:
            score.reset()
            snack.reset()


screen.exitonclick()