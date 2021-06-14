from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-180, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 66, "normal"))
        self.goto(180, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 66, "normal"))

    def l_scoree(self):
        self.l_score += 1
        self.update_score()

    def r_scoree(self):
        self.r_score += 1
        self.update_score()



