from turtle import *
from PIL import Image
import pandas as pd

o_i = Image.open("india_image.gif")
o_i = o_i.resize((800,800))
o_i.save("india_image.gif")


screen = Screen()
screen.title("Indian States Game")
image ="india_image.gif"
screen.addshape(image)
screen.setup(700,750)
shape(image)

# the below gives the x,y coordinates since we have already have them this is not neccesary

# def click_on_coor(x,y):
#     print(x,y)

# onscreenclick(click_on_coor)
# mainloop()
guessed_states =[]
df = pd.read_csv("data_states.csv")
states= df.state.to_list()
while len(guessed_states)<len(states):

    answer_guess = (screen.textinput(title=f"{len(guessed_states)}/29 States Correct", prompt="What is another state name"))
    answer_guess = answer_guess.title()
    if answer_guess == "Exit":
        missing_states=[]
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
                df = pd.DataFrame(missing_states)
                df.to_csv("missed_states.csv")

        break

    if answer_guess in states:
        data_state = df[df.state==answer_guess]
        if answer_guess not in guessed_states:
            guessed_states.append(answer_guess)
        else:
            print("Already completed")
        x_g = int(data_state.x)
        # print(type(data_state['x'])) # <class 'pandas.core.series.Series'>
        y_g = int(data_state.y)
        # print(type(y_g)) # <class 'int'>

        s = Turtle()
        s.hideturtle()
        s.penup()
        s.goto(x_g,y_g)
        s.write(answer_guess)
        # s.write(data_state.state.item(), font=("Arial", 8, "normal"))    
        
    else:
        print("Wrong Guess")



# print(data_state)
# print(x_g)
# print(y_g)
