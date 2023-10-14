import turtle as t
import pandas

screen = t.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game by @Emilio_Morles")

image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
us_states = data.state
us_states_list = us_states.to_list()
# print(us_states_list)  # pandas print everything in order.

# def get_mouse_click_coor(x, y):
#     """This code allow me to find the coordinates in the screen by clicking the mouse""" 👀
#     print(x, y)
#
#
# t.onscreenclick(get_mouse_click_coor)
#
# t.mainloop()

guessed_states = []  # It records the correct states guessed

while len(guessed_states) < 51:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()  # It writes the answer in title.
    # And allow the user to track of the score.
    answer_state_t = answer_state.title()
    # print(answer_state_t)

    if answer_state_t == "Exit":
        missing_states = []
        for state in us_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")  # It creates a file with all the missing states
        break

    if answer_state_t in us_states_list:  # If answer_state is one of the states in all states of the 50_states.csv
        # Create a turtle to write the name of the state at the state's s x and y coordinate
        guessed_states.append(answer_state_t)
        state_name = t.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_data = data[data.state == answer_state_t]  # I LEARNED THIS 👀
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(state_data.state.item())  # In Pandas. It returns the first element of the underlying data as a
        # Python scalar. Link https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html 👀
