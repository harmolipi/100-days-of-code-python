from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        """Create a snake object."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        for i in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(x=-20 * i, y=0)
            self.segments.append(snake_segment)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self) -> None:
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position) -> None:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())
