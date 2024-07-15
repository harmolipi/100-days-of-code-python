from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
my_screen = Screen()

# Draw a square
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# Draw a dashed line
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

my_screen.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)


def draw_shape(num_sides):
    tim.pencolor(random_color())
    angles = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angles)


def draw_the_shapes():
    for sides in range(3, 11):
        draw_shape(sides)


# draw_the_shapes()


def walk_and_turn():
    directions = [0, 90, 180, 270]
    tim.pencolor(random_color())

    tim.forward(38)
    tim.setheading(choice(directions))


def random_walk():
    tim.pensize(15)
    tim.speed("fastest")

    for _ in range(200):
        walk_and_turn()


# random_walk()


def spirograph(num_circles):
    tim.speed("fastest")
    angle = 360 / num_circles

    for _ in range(num_circles):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.right(angle)


spirograph(100)
my_screen.exitonclick()
