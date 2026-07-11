import tkinter as tk
from tkinter import messagebox as mbox
import random as rnd
import json
import pyperclip

# ==============================
# Constants
# ==============================

IMG_WI = 200
IMG_HI = 200
PAD = 50

# ==============================
# Password generator
# ==============================

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [rnd.choice(letters) for _ in range(rnd.randint(8, 10))]
    password_symbols = [rnd.choice(symbols) for _ in range(rnd.randint(2, 4))]
    password_numbers = [rnd.choice(numbers) for _ in range(rnd.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    rnd.shuffle(password_list)

    password = "".join(password_list)
    pass_ent.insert(0, password)

# ==============================
# SAVE PASSWORD
# ==============================

def save_data():

    # Get entries
    website = web_ent.get()
    email = user_ent.get()
    password = pass_ent.get()

    # Store them in a dictionary
    new_data = {
        website: {
            "email: ": email,
            "password: ": password,
        }
    }

    # Show an error box if they did not fill the filed
    if len(website)==0 or len(password)==0:
        error_1 = mbox.showerror("Error", "Please fill all fields!")

    else:
        # Confirm the inputs
        is_ok = mbox.askokcancel(title=website, message=f"Entered Information: \nEmail: {email}\nPassword: {password}"
                                        f"\n\nDo you want to save them?")
        if is_ok:

            # Load the data
            try:
                with open("passwords.json", "r") as file:
                    # Load storage data
                    data = json.load(file)

            # If not possible: Create one
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    # Add the data to newly created storage file
                    json.dump(new_data, file, indent=4)

            # if try worked
            else:
                # Update data in this code
                data.update(new_data)

                with open("passwords.json", "w") as file:
                    # Save updated data
                    json.dump(data, file, indent=4)

            finally:
                web_ent.delete(0, len(website))
                pass_ent.delete(0, len(password))
                pyperclip.copy(password)

# =========================================
# Search the storage for a password
# =========================================

def search_storage():

    wanted_website = web_ent.get()

    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        mbox.showinfo(title="Error", message="No Data File Found.")
    else:
        if wanted_website in data:
            wanted_email = data[wanted_website]["email: "]
            wanted_password = data[wanted_website]["password: "]
            mbox.showinfo(title=wanted_website, message=f"Email: {wanted_email}\nPassword: {wanted_password}\nPassword has been copied in your clipboard!")
            pyperclip.copy(wanted_password)
        else:
            mbox.showinfo(title="Error", message=f"No details for {wanted_website} exists.")
    finally:
        web_ent.delete(0, len(wanted_website))
        pass_ent.delete(0, len(wanted_website))

# ==============================
# Window set-up
# ==============================

# Window of the GUI
window = tk.Tk()
window.title("Password Manager")
window.config(padx=PAD, pady=PAD, bg="white")

# Configure grid columns to have equal weight for better spacing
window.columnconfigure(0, weight=0)  # Label column
window.columnconfigure(1, weight=1)  # Entry column
window.columnconfigure(2, weight=0)  # Button column

# Logo Image
canvas = tk.Canvas(width=IMG_WI, height=IMG_HI, bg="white", highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(IMG_WI/2, IMG_HI/2, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# ==============================
# UI set-up
# ==============================

# ---------- Website ---------- #

# Label
web_lab = tk.Label(text="Website:", bg="white", font=("Arial", 10, "bold"))
web_lab.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)

# Frame for putting entry + button in a row
website_frame = tk.Frame(window, bg="white")
website_frame.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)

# Entry
web_ent = tk.Entry(website_frame, width=21, bg="white", font=("Arial", 10))
web_ent.pack(side="left", fill="x", expand=True)

# Generate Password button
search_btn = tk.Button(website_frame, text="Search", bg="#f9d3d6", fg="black", command=search_storage, font=("Arial", 9))
search_btn.pack(side="left", padx=(5, 0))

# ---------- Username/Gmail ---------- #

# Label
user_lab = tk.Label(text="Email/Username:", bg="white", font=("Arial", 10, "bold"))
user_lab.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)

# Entry
user_ent = tk.Entry(width=35, bg="white", font=("Arial", 10))
user_ent.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)

# Default entry (my email)
user_ent.insert(0, "najmehnayyer@gmail.com")

# ---------- Username/Gmail ---------- #

# Label
pass_lab = tk.Label(text="Password:", bg="white", font=("Arial", 10, "bold"))
pass_lab.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)

# Frame for putting entry + button in a row
password_frame = tk.Frame(window, bg="white")
password_frame.grid(row=3, column=1, columnspan=2, sticky="ew", pady=5)

# Entry
pass_ent = tk.Entry(password_frame, width=21, bg="white", font=("Arial", 10))
pass_ent.pack(side="left", fill="x", expand=True)

# Generate Password button
passgen_btn = tk.Button(password_frame, text="Generate Password", bg="white", fg="black", command=generate_password, font=("Arial", 9))
passgen_btn.pack(side="left", padx=(5, 0))

# ---------- Add the password ---------- #

# Button
add_btn = tk.Button(window, text="Add", bg="white", fg="black", width=30, command=save_data, font=("Arial", 10, "bold"))
add_btn.grid(row=4, column=1, columnspan=2, sticky="ew", pady=(15, 0))

window.mainloop()
