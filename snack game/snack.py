from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180



class Snack:
    def __init__(self):
        self.snacks=[]
        self.create_snack()
        self.head = self.snacks[0]
    def create_snack(self):
        for position in STARTING_POSITION:
            self.add(position)



    def add(self,position):

        snack=Turtle()
        snack.shape("square")
        snack.color("white")
        snack.penup()
        snack.goto(position)
        self.snacks.append(snack)

    def reset(self):
        for seg in self.snacks:
            seg.goto(1000,1000)
        self.snacks.clear()
        self.create_snack()
        self.head = self.snacks[0]  # ← Reassign the new head here

    def extand(self):
        self.add(self.snacks[-1].position())




    def move(self):
        for sag in range(len(self.snacks)-1,0,-1):
                new_x=self.snacks[sag-1].xcor()
                new_y=self.snacks[sag-1].ycor()
                self.snacks[sag].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)