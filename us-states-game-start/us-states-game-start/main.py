import turtle
import pandas


data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

count = 0
answered = []
check_answer = data.state.to_list()
game_is_on = True
while game_is_on:
    timmy = turtle.Turtle()
    if count > 0:
        answer_state = screen.textinput(title=f"{count}/50 correct answers", prompt="What is the name of the state?")
    else:
        answer_state = screen.textinput(title="Guess state name", prompt="What is the name of the state?")
    # print(answer_state)
    answer_state = answer_state.title()

    # check_answer = data.state.to_list()
    # x = data["x"].to_list()
    # y = data["y"].to_list()
# check if answer_state in the state list
    if answer_state == "Exit":
        # list comprehension
        state_learn = [state for state in check_answer if state not in answered]
        # for i in check_answer:
        #     if i not in answered:
        #         state_learn.append(i)
        data_dict = {
            "states to learn": state_learn,
        }

        data_state = pandas.DataFrame(data_dict)

        data_state.to_csv("States_to_learn.csv")
        break
    if answer_state in check_answer and answer_state not in answered:
        timmy.hideturtle()
        timmy.penup()
        # index = check_answer.index(answer_state)
        # print(x[index], "   ", y[index])
        # x_value = x[index]
        # y_value = y[index]
        state_data = data[data.state == answer_state]
        timmy.goto(x=int(state_data.x), y=int(state_data.y))
        # timmy.goto(x=x_value, y=y_value)
        timmy.write(arg=f"{answer_state}", align="center", font=('calibiri', 8 , "normal"))
        count += 1
        print(count)
        answered.append(answer_state)
        if count >= 50:
            game_is_on = False


# print(data_dict)
# screen.exitonclick()
