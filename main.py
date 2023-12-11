from turtle import *
from pandas import *


writer = Turtle()
writer.penup()
writer.hideturtle()

score = 0

screen = Screen()
screen.setup(740, 510)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle(image)
turtle.penup()

data = read_csv("50_states.csv")

states = data.state.to_list()

answers = []
game_is_on = True
while game_is_on:
    answer = screen.textinput(f"You have {score}/50 state", "Guess a name of a state").lower()
    answer = answer.strip()
    if answer in ["exit", "off"]:
        game_is_on = False
        writer.goto(0, 0)
        writer.pencolor("red")
        writer.write(f"Thanks for the Game.\n"
                     f"Your score was {score}/50 !", False, "center", ("Comic Sans", 25, "normal"))
    else:
        for state in states:
            if answer == state.lower() and state not in answers:
                answer = state
                score += 1
                answers.append(answer)
                df = data[data.state == answer]
                writer.goto(df.x.iloc[0], df.y.iloc[0])
                writer.write(f"{answer}", False, "center", ("Comic Sans", 10, "normal"))
    if score == 50:
        game_is_on = False
        writer.goto(0, 0)
        writer.pencolor("green")
        writer.write("     Congratulations! "
                     "\nYour score was 50/50 .", False, "center", ("Comic Sans", 25, "normal"))

missing_states = {"state": [state for state in states if state not in answers],
                  "x": [data[data.state == state].x.iloc[0] for state in states if state not in answers],
                  "y": [data[data.state == state].y.iloc[0] for state in states if state not in answers]}

new_data = DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

# screen.exitonclick()
