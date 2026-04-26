
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore= int(data.read())
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.write(f" score={self.score} high score={self.highscore}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):

        self.score+=1
        self.update()



