from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(x=-270, y=260)
        self.pendown()
        self.writing()
        self.hideturtle()

    def writing(self):
        self.clear()
        self.write(arg=f"Level: {self.level} ", move=False, align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.writing()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(arg=f"Game Over", align="center", font=FONT)

