from turtle import Turtle
STYLE = ('Courier', 10, 'normal')
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", False, align=ALIGNMENT, font=STYLE)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=STYLE)

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

