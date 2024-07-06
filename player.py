from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.restart()
        self.score: int = 0

    def move_forwards(self) -> None:
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def restart(self) -> None:
        self.clear()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def is_at_finish_line(self) -> bool:
        return self.ycor() >= FINISH_LINE_Y
