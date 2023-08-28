from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ast

def register():
    """Handle the registration process."""
    username_val = username_entry.get()
    password_val = password_entry.get()

    # Check if any of the fields are empty
    if not username_val or not password_val:
        messagebox.showerror("Registration Failed", "Please fill in all the fields")
        return

    # File path
    file_path = "user_data.txt"

    # Create a dictionary to store the user data
    user_data = {
        'username': username_val,
        'password': password_val,
    }

    # Read existing data from the text file
    existing_data = {}
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                existing_data = ast.literal_eval(data)
    except FileNotFoundError:
        pass

    # Check if the username already exists
    if username_val in existing_data:
        messagebox.showerror("Registration Failed", "Username already exists")
        return

    # Add the new user data to the existing data
    existing_data[username_val] = user_data

    # Write the updated data to the file
    with open(file_path, 'w') as file:
        file.write(str(existing_data))

    messagebox.showinfo("Registration Successful", "Registration successful. Please log in.")
    root.destroy()
    import Login

root = Tk()
root.config(bg='black', padx=100, pady=70)
root.title("Register")
root.geometry('800x500+50+50')
root.resizable(False, False)

# Load the image
register_image = PhotoImage(file="Assets/register.png")

# Display the image
register_image_label = Label(root, image=register_image)
register_image_label.place(x=50, y=0)

# Create username and password entry widgets
username = StringVar()
password = StringVar()

username_entry = Entry(root, textvariable=username, font=('Arial', 12), relief=FLAT)
username_entry.place(x=320, y=180)

password_entry = Entry(root, textvariable=password, show='*', font=('Arial', 12), relief=FLAT)
password_entry.place(x=320, y=240)

# Create labels
username_label = Label(root, text="Username:", font=('Arial', 12), bg='white')
username_label.place(x=220, y=180)

password_label = Label(root, text="Password:", font=('Arial', 12), bg='white')
password_label.place(x=220, y=240)

# Create register button
register_button = Button(root, text="Register", command=register, font=('Arial', 12), bg="#57a1f8", fg='white')
register_button.place(x=320, y=300)

# Run the program
root.mainloop()
