# import colorgram

# colors = colorgram.extract("image.jpg", 25)


# def get_rgbs(color):
#     return (color.rgb.r, color.rgb.g, color.rgb.b)


# rgb_array = map(get_rgbs, colors)

# print(list(rgb_array))

from turtle import Turtle, Screen
import random

image_colors = [
    (199, 169, 95),
    (229, 240, 233),
    (129, 179, 191),
    (162, 56, 77),
    (234, 221, 121),
    (50, 114, 167),
    (106, 89, 86),
    (240, 213, 219),
    (142, 186, 122),
    (215, 152, 171),
    (67, 125, 76),
    (95, 124, 180),
    (85, 166, 95),
    (232, 241, 247),
    (191, 68, 89),
    (160, 35, 49),
    (142, 120, 116),
    (218, 174, 183),
    (199, 120, 52),
    (175, 204, 176),
    (160, 203, 213),
    (66, 56, 51),
    (177, 189, 213),
    (73, 60, 57),
]

my_turtle = Turtle()
my_screen = Screen()

my_screen.exitonclick()
my_screen.colormode(255)
my_screen.screensize(2000, 1500)

print(random.choice(image_colors))

for _ in range(10):

    for _ in range(10):
        my_turtle.pendown()
        my_turtle.dot(20, random.choice(image_colors))
        my_turtle.penup()
        my_turtle.forward(50)

    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.left(180)
