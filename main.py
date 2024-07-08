import turtle

import pandas

states_data = pandas.read_csv("./50_states.csv")
lowercase_states = states_data["state"].map(lambda state: str.lower(state))

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answers_turtle = turtle.Turtle()
answers_turtle.speed("fastest")
answers_turtle.penup()
answers_turtle.hideturtle()
answers_turtle.goto(0, 0)

correct_answers = []

game_is_on = True


def plot_answer(state: pandas.Series):
    x = int(state.x)
    y = int(state.y)
    state_name = state.state.item()

    answers_turtle.goto((x, y))
    answers_turtle.write(state_name)


while game_is_on:
    answer_state = screen.textinput(
        f"{len( correct_answers )}/50 States Correct", "What's another state name?"
    )

    if answer_state is None:
        continue

    answer_state = answer_state.title()
    found_state = states_data[states_data.state == answer_state]

    if answer_state in correct_answers:
        continue

    if len(found_state) == 1:
        correct_answers.append(answer_state)
        plot_answer(found_state)

screen.exitonclick()
