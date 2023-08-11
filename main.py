from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generatePassword():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]
    password_numbers = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_letter+password_symbols+password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    if len(website) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Warning", message="You left some fields empty")
    else:
        isOk = messagebox.askokcancel(
            title=website,
            message=f"These are the details you entered:\nEmail:{email}\nPassword:{password}\npress OK to save it"
        )
        if isOk:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(
    padx=50,
    pady=50
)
canvas = Canvas(
    window,
    width=200,
    height=200,
)
logoPNG = PhotoImage(
    file="logo.png"
)
canvas.create_image(
    100,
    100,
    image=logoPNG
)
canvas.grid(
    row=0,
    column=1
)

websiteLabel = Label(text="Website:")
websiteLabel.grid(
    row=1,
    column=0
)
emailLabel = Label(text="Email/Username:")
emailLabel.grid(
    row=2,
    column=0
)
passwordLabel = Label(text="Password:")
passwordLabel.grid(
    row=3,
    column=0
)
websiteEntry = Entry(width=35)
websiteEntry.grid(
    row=1,
    column=1,
    columnspan=2
)
emailEntry = Entry(width=35)
emailEntry.grid(
    row=2,
    column=1,
    columnspan=2
)
emailEntry.insert(
    0,
    "AbdalrhmanExample@yahoo.com"
)
passwordEntry = Entry(width=25)
passwordEntry.grid(
    row=3,
    column=1,
    sticky=E
)
generatePasswordBtn = Button(text="Generate Password", height=1, width=15, command=generatePassword)
generatePasswordBtn.grid(
    row=3,
    column=2,

)
addBtn = Button(text="Add", width=36, command=save)
addBtn.grid(
    row=4,
    column=1,
    columnspan=2
)

window.mainloop()
