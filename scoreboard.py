from turtle import Turtle

POSITION = "center"
FONT_SIZE = ("Courier", 80, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.goto(position)
        self.write(f"{self.score}", align= POSITION, font= FONT_SIZE)



