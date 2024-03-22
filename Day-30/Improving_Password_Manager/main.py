import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Copy", message="The password has been copied to your clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get().title()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(password) == 0 or len(username) == 0 or len(website) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, "end")
            website_entry.delete(0, "end")


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave website empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                information = data[website]
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")
        except KeyError:
            messagebox.showerror(title="Error", message=f"No details for the {website} exists")
        else:
            pyperclip.copy(information["password"])
            messagebox.showinfo(title=website, message=f"Username: {information["username"]}\n"
                                                       f"Password: {information["password"]}")
            messagebox.showinfo(title="Password Copy", message="The password has been copied to your clipboard.")
        finally:
            website_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

username_label = tkinter.Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=33)
website_entry.grid(column=1, row=1, )
website_entry.focus()

username_entry = tkinter.Entry(width=54)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "tarkangur13@gmail.com")

password_entry = tkinter.Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = tkinter.Button(text="Generate Password", width=16, bg="white", highlightthickness=0,
                                 command=generate_password)
generate_button.grid(column=2, row=3)

search_button = tkinter.Button(text="Search", width=16, bg="white", highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1)

add_button = tkinter.Button(text="Add", width=46, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
