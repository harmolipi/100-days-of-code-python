from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.restart()
        self.score = 0

    def move_forwards(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def restart(self):
        self.clear()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
