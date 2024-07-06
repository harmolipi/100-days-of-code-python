from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def increment_score(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 260)
        self.write(
            f"Level: { self.level }", align="center", font=("Monospace", 25, "normal")
        )

    def show_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Monospace", 25, "normal"))
