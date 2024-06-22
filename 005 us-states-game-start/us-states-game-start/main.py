import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. states game")
images="blank_states_img.gif"
screen.addshape(images)
turtle.shape(images)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_states=screen.textinput(title=f"{len(guessed_states)}/50 States correct",prompt="Whats the another states name").title()
    if answer_states=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")      
        break
    if answer_states in all_states:
        guessed_states.append(answer_states)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_states]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_states,align="center",font="Arial")


