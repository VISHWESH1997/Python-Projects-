from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_numbers + password_symbols + password_letter
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    website_info = website_input.get()
    email_info = email_input.get()
    password_info = password_input.get()
    new_data = {website_info:
        {
            "email": email_info,
            "password": password_info
        }}
    website_len = len(website_info)
    password_len = len(password_info)
    if password_len <= 0 or website_len <= 0:
        messagebox.showinfo(title="OOPS!!!", message="No fields must be kept empty")
    else:
        is_ok = messagebox.askokcancel(title=website_info, message=f"Is the website: {website_info} \n"
                                                                   f" password: {password_info} \n that you have "
                                                                   f"entered correct?")
        if is_ok:
            try:
                with open("password.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("password.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                # read old data
                # data = json.load(f)
                # update old data with new
                data.update(new_data)
                # save updated data
                with open("password.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- Find Password ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("password.json", "r") as f:
            data_dict = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File is not available")
    else:
        # for i in data_dict:
        #     if website == i:
        if website in data_dict:
            messagebox.showinfo(title="Password Found", message=f"email: {data_dict[website]['email']}"
                                                                f" \n password:{data_dict[website]['password']} ")
            # print(f"email: {data_dict[i]['email']} \n password:{data_dict[i]['password']} ")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} available")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
# row starts at 0 column starts at 1

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=2)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(row=1, column=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
email_label.grid(row=2, column=1)

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(row=3, column=1)
# password_label.config(padx=20,pady=0)

# Entry boxes

website_input = Entry(width=32)
website_input.grid(row=1, column=2, sticky='EW')
website_input.focus()

email_input = Entry(width=45)
email_input.grid(row=2, column=2, columnspan=2, sticky='EW')
email_input.insert(0, "vishweshvaidy97@gmail.com")

password_input = Entry(width=32)
password_input.grid(row=3, column=2, sticky='ew')

# buttons

add_button = Button(text="Add", width=50, command=add_info)
add_button.grid(row=4, column=2, columnspan=2)

password_button = Button(text="Generate Password", width=20, command=generate_password)
password_button.grid(row=3, column=3)

search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(row=1, column=3, sticky='ew')

window.mainloop()
