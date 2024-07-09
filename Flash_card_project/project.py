from tkinter import *
import pandas as pd
import random

# ^.*[STRING].*$\n regular exp for removing line

BACKGROUND_COLOR = "#B1DDC6"
text = {}
dictionary_t={}
try:
    df = pd.read_csv("still_learning.csv")
except FileNotFoundError:
    df = pd.read_csv("Frequency_french.csv")
    dictionary_t= df.to_dict(orient="records")
else:
    dictionary_t = df.to_dict(orient="records")


def change_word():
    global text, flip_timer
    window.after_cancel(flip_timer)
    # if card is in french using directly
    text =random.choice(dictionary_t)
    canvas.itemconfig(card_text,text=text['French'],fill="black")
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(canvas_image,image=front_img)
    flip_timer=window.after(3000, func=flip_card)   

    
def flip_card():
    canvas.itemconfig(card_text,text=text['English'],fill="white")
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(canvas_image,image=back_img)

def known():
    dictionary_t.remove(text)
    print(len(dictionary_t))
    df = pd.DataFrame(dictionary_t)
    df.to_csv("still_learning.csv",index=False)
    change_word()

window = Tk()
window.title("Flashy Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)   

canvas = Canvas(height=526, width=800)

front_img = PhotoImage(file ="images/card_front.png")
back_img = PhotoImage(file ="images/card_back.png")

canvas_image=canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)
card_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_text=canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))


correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image,highlightthickness=0,command=known)
correct_button.config(pady=50,padx=10)
correct_button.grid(row=1, column=1)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=change_word)
wrong_button.config(pady=50,padx=10)
wrong_button.grid(row=1, column=0)

change_word()

window.mainloop()
