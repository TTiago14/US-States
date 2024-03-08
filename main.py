import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
guessed_states = []

while len(guessed_states) < 51:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "End":
        user_states = pandas.DataFrame(guessed_states)
        user_states.to_csv("guessed_states.csv")
        break


    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        score += 1
        guessed_states.append(state_data.state.item())
        print(guessed_states)



