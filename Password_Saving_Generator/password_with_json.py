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
import json

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
    
    new_entry = {
        "email": username.lower(),
        "password": password
    }

    if not password or not username or not website:
        messagebox.showinfo(title="Oops", message="Don't leave any field empty")
    else:
        try:
            with open("save_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("save_data.json", "w") as file:
                json.dump(new_entry, file, indent=4)

        except json.decoder.JSONDecodeError:
            data = {}
        if website in data:
            data[website].append(new_entry)
        else:
            data[website] = [new_entry]
        
        with open("save_data.json", "w") as file:
            json.dump(data, file, indent=4)
        
        entry_password.delete(0, END)
        entry_emuser.delete(0, END)
        entry_web.delete(0, END)

def find_password():
    website = entry_web.get()
    email = entry_emuser.get()
    try:
        with open("save_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if website in data:
            if len(email)==0:
                entries = data[website]
                entry_details = "\n\n".join([f"Email: {entry['email']}\nPassword: {entry['password']}" for entry in entries])
                messagebox.showinfo(title=website, message=entry_details)
            else:
                for entry in data[website]:
                    if entry["email"] == email:
                        messagebox.showinfo(title=website, message=f"Email: {entry['email']}\nPassword: {entry['password']}")
        else:
            messagebox.showinfo(title="Oops", message=f"No Details for the website: {website} exist")


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

entry_web = Entry(width=22)
entry_web.config(bg='white')
entry_web.grid(column=1, row=1, columnspan=1)
entry_web.focus()

search_button = Button(text="Search",width=15,height=1,command=find_password)
search_button.config(bg='white',pady=1)
search_button.grid(column=2, row=1, columnspan=1)

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
