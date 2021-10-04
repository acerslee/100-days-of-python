from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.write(f"{self.l_score} : {self.r_score}",False, ALIGNMENT, FONT)

    def add_score(self, side):
        self.clear()
        if side == "right":
            self.r_score += 1
        else:
            self.l_score += 1
        self.write(f"{self.l_score} : {self.r_score}",False, ALIGNMENT, FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)