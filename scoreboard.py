# Bhavay garg
# This class keeps track of the score

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, 'normal')


class ScoreKeeper(Turtle):
    def __init__(self):
        super().__init__()
        # we can get hold of the core here by using self.score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)

    def score_keeping(self, current_score):
        self.clear()
        self.write(f"Score : {current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)

        self.write("GAME OVER", align="center", font=FONT)