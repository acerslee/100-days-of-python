from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.write(f"Score: {self.score}",False, ALIGNMENT, FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)