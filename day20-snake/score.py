from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

with open("data.txt") as file:
    score = file.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(0)
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()
