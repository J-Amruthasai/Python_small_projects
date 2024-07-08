'''
This is actually for Password saving for a website and email 
it can also if you dont want to think about password 
it will help us by generating a password
where the password will copied to clipboard we can paste it where ever we want

'''

from tkinter import *
import string
import random
import pyperclip
# imports classes and constants
# so like messagebox will not be imported
from tkinter import messagebox
# from PIL import Image

# o_i = Image.open("password_manager_logo.png")
# o_i = o_i.resize((200,200))
# o_i.save("password_manager_logo.png")

def genrate_password():
    alphabets = list(string.ascii_letters)
    letters_took = [random.choice(alphabets) for _ in range(random.randint(8,10))]

    sym = list(string.punctuation)
    symbols_took = [random.choice(sym) for _ in range(random.randint(2,4))]

    digits = ["1","2","3","4","5","6","7","8","9","0"]
    numbers_took = [random.choice(digits) for _ in range(random.randint(2,4))]

    pass_list = symbols_took+letters_took+numbers_took
    random.shuffle(pass_list)
    password = "".join(pass_list)
    # entry_password.insert(0,password)
    pyperclip.copy(password)
    return password

def save():
    password = entry_password.get()
    username = entry_emuser.get()
    website = entry_web.get()

    if password == "" or username == "" or website == "" :
        messagebox.showinfo(tiltle="Oops", message="Don't leave any field empty")
    else:
    # messagebox.showwarning(tiltle="hello", message="Hey!")
        noyes=messagebox.askokcancel(title = website,message=f"These are the details: \nEmail: {username}\nPassword: {password} \nIs it ok to save?")
    if noyes:
        with open("save_data.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")
        entry_password.delete(0, END)
        entry_emuser.delete(0, END)
        entry_web.delete(0, END)

window = Tk()
window.title("Password Generator")
window.config(padx=10, pady=10, bg='white')

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file ="images.png")
canvas.create_image(100, 100, image=logo_img)
canvas.config(bg='white', highlightthickness=0)
canvas.grid(column=1, row=0)

website =Label(text="Website:",font=("Arial",12,"bold"))
website.config(bg='white',pady=5)
website.grid(column=0, row=1)

entry_web = Entry(width=40)
entry_web.config(bg='white')
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()

emuser =Label(text="Email/Username: ",font=("Arial",12,"bold"))
emuser.config(bg='white',pady=5)
emuser.grid(column=0, row=2)

entry_emuser = Entry(width=40)
entry_emuser.config(bg='white')
entry_emuser.grid(column=1, row=2, columnspan=2)
# entry_emuser.insert()

password =Label(text="Password: ",font=("Arial",12,"bold"))
password.config(bg='white',pady=5)
password.grid(column=0, row=3)

entry_password = Entry(width=22)
entry_password.config(bg='white')
entry_password.grid(column=1, row=3, columnspan=1)

generated_button = Button(text="Generate Password",width=15,height=1, command=genrate_password)
generated_button.config(bg='white',pady=1)
generated_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add",width=38,command = save)
add_button.config(bg='white',pady=1)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()












import tkinter
import math

# Color Constants
BLACK = "#151515"
WHITE = "#FFFFFF"
GREY = "#EEEEEE"
RED = "#C73659"
MAROON = "#A91D3A"
ORANGE = "#E0A75E"
YELLOW = "#F9D689"
BEIGE = "#F5E7B2"
GREEN = "#00FF00"

# Font Constants
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

rep = 0
timer = None
is_running = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, rep, is_running
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=WHITE)
    label_2.config(text="")
    rep = 0
    is_running = False

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep, is_running
    if is_running:
        return
    is_running = True
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if rep % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text="Break", fg=RED)
       
    elif rep % 2 == 0:
        count_down(short_break_sec)
        label_1.config(text="Break", fg=MAROON)
      
    else:
        count_down(work_sec)
        label_1.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global is_running
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        is_running = False
        start_timer()
        marks = ""
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_2.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=BLACK)

label_1 = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=BLACK, fg=WHITE)
label_1.grid(column=1, row=0)

canvas = tkinter.Canvas(width=212, height=224, bg=BLACK, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(106, 112, image=tomato_img)
timer_text = canvas.create_text(106, 132, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Commented out the section for setting work time
# def set_work_time():
#     global WORK_MIN
#     WORK_MIN = int(work_time_entry.get())
#     label_1.config(text=f"Work Time Set to {WORK_MIN} min", fg=GREEN)

# work_time_label = tkinter.Label(text="Set Work Time (min):", font=(FONT_NAME, 12, "bold"), bg=BLACK, fg=WHITE)
# work_time_label.grid(column=0, row=2)
# work_time_entry = tkinter.Entry(width=5)
# work_time_entry.grid(column=1, row=2)
# set_time_button = tkinter.Button(text="Set", font=(FONT_NAME, 12, "bold"), command=set_work_time)
# set_time_button.grid(column=2, row=2)

button_start = tkinter.Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer, bg=WHITE, fg=RED)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer, bg=WHITE, fg=RED)
button_reset.grid(column=2, row=2)

label_2 = tkinter.Label(font=(FONT_NAME, 35), bg=BLACK, fg=GREEN)
label_2.grid(column=1, row=3)

window.mainloop()