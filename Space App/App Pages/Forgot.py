"""
Import Modules
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import ast

# Function to create a new password
def create_new_password():
    """
    Create a new password for the given username.

    Reads the username and new password from the respective entry fields,
    then saves the new password to the datasheet.txt file if the username exists.
    """
    username = username_entry.get()
    new_password = new_password_entry.get()

    if username and new_password:
        # Save the new password to the datasheet.txt file
        file_path = "datasheet.txt"
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                data = ast.literal_eval(data)

            if username in data:
                data[username]['password'] = new_password
                with open(file_path, 'w') as file:
                    file.write(str(data))
                messagebox.showinfo("New Password", f"New password for {username} has been saved.")
            else:
                messagebox.showerror("Error", "Username not found in the data file.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found. Please ensure datasheet.txt exists.")

    else:
        messagebox.showerror("Error", "Please enter a username and a new password.")

# Function to show/hide the password
def toggle_password_visibility():
    """
    Toggle the visibility of the new password.

    This function toggles the visibility of the new password entry field
    and updates the corresponding button label accordingly.
    """
    if new_password_entry['show'] == '*':
        new_password_entry['show'] = ''
        hide_button.config(text="Hide Password")
    else:
        new_password_entry['show'] = '*'
        hide_button.config(text="Show Password")

# Function to show the "Create Password" entry field
def show_create_password_entry():
    """
    Show the "Create Password" entry field.

    This function displays the entry field and related components for creating a new password.
    """
    reset_button.grid_forget()
    new_password_entry.grid(row=5, column=1, pady=15, columnspan=2)
    new_password_line.grid(row=6, column=1, pady=0, columnspan=2)
    hide_button.grid(row=7, column=1, pady=15, columnspan=2)
    create_button.grid(row=8, column=1, pady=15, columnspan=2)
    # Label for new password entry
    new_password_label = tk.Label(container, text="Enter Your New Password Here:", font=('Microsoft Yahei UI light', 10), fg="#57a1f8", bg="white")

# Function to handle the insertion of default text when entry gains focus
def on_focus_in(default_text, entry_widget, line_widget):
    """
    Handle the insertion of default text when entry gains focus.

    This function is called when an entry widget gains focus.
    If the entry contains the default text, it is cleared.
    """
    if entry_widget.get() == default_text:
        entry_widget.delete(0, END)
    line_widget.config(bg="#57a1f8")

# Function to handle the deletion of default text when entry loses focus
def on_focus_out(default_text, entry_widget, line_widget):
    """
    Handle the deletion of default text when entry loses focus.

    This function is called when an entry widget loses focus.
    If the entry is empty, it is filled with the default text.
    """
    if entry_widget.get() == "":
        entry_widget.insert(0, default_text)
    line_widget.config(bg="black")

# Function to check if the username exists
def check_username_exists():
    """
    Check if the given username exists in the data file.

    This function reads the username from the entry field
    and checks if it exists in the data file (datasheet.txt).
    If the username exists, the "Create Password" entry field is shown.
    """
    username = username_entry.get()
    if username:
        try:
            with open("datasheet.txt", "r") as file:
                data = file.read()
                data = ast.literal_eval(data)
                if username in data:
                    show_create_password_entry()
                else:
                    messagebox.showerror("Error", "Username not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found. Please ensure datasheet.txt exists.")
    else:
        messagebox.showerror("Error", "Please enter a username.")

# Previous page function
def previousPage():
    """
    Navigate to the previous page (Login page).

    This function destroys the current application window and loads the Login page.
    """
    root.destroy()
    import Login

# Next page function
def previousPage1():
    """
    Navigate to the next page (Registration page).

    This function destroys the current application window and loads the Registration page.
    """
    root.destroy()
    import Register

# Setup the main application window
root = Tk()
root.config(bg='grey')
root.title("App")
root.geometry('550x700')
root.resizable(False, False)

# Load the background image
background_image = PhotoImage(file="Assets/background.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a white box to contain the widgets
container = Frame(root, bg="white")
container.place(relx=0.5, rely=0.5, anchor="center")

# Create and place the widgets inside the container
label = tk.Label(container, text="Forgot Password?", font=('Microsoft Yahei UI light', 20), fg="#57a1f8", pady=10, bg="white")
label.grid(row=0, column=0, pady=30, columnspan=4)

# Username entry field
default_username_text = "Username or Email"
username_entry = tk.Entry(container, width=30, border=0, highlightthickness=0, fg="#57a1f8")
username_entry.grid(row=1, column=1, pady=10, columnspan=2)
username_entry.insert(0, default_username_text)
username_entry.bind("<FocusIn>", lambda event: on_focus_in(default_username_text, username_entry, username_line))
username_entry.bind("<FocusOut>", lambda event: on_focus_out(default_username_text, username_entry, username_line))
username_line = Canvas(container, width=200, height=2.0, bg='black', highlightthickness=0)
username_line.grid(row=2, column=1, pady=0, columnspan=2)

# Button to check if the username exists
check_username_button = tk.Button(container, text="Check Username", command=check_username_exists, font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)
check_username_button.grid(row=3, column=1, pady=15, columnspan=2)

# Button to show the "Create Password" entry field
reset_button = tk.Button(container, text="Reset Password", command=lambda: show_create_password_entry(container), font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)

# Create a new password entry (Initially hidden)
default_password_text = "Type your new password here"
new_password_entry = tk.Entry(container, show='', width=30, border=0, highlightthickness=0, fg="#57a1f8")
new_password_entry.insert(0, default_password_text)
new_password_entry.bind("<FocusIn>", lambda event: on_focus_in(default_password_text, new_password_entry, new_password_line))
new_password_entry.bind("<FocusOut>", lambda event: on_focus_out(default_password_text, new_password_entry, new_password_line))
new_password_line = Canvas(container, width=200, height=2.0, bg='black', highlightthickness=0)

# Button to show/hide the password
hide_button = tk.Button(container, text="Hide Password", command=toggle_password_visibility, font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)

# Button to create the new password
create_button = tk.Button(container, text="Reset Password", command=create_new_password, font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)

# Already have account button
already_have_account_button = Button(container, text="Already Have an Account? Login!", command=previousPage, fg="black", bg="white", font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
already_have_account_button.grid(row=9, column=0, pady=15, columnspan=4)

# Create account button
account_button = Button(container, text="Don't have an account? Create One!", command=previousPage1, fg="black", bg="white", font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
account_button.grid(row=10, column=0, pady=0, columnspan=4)

#Run the GUI mainloop
root.mainloop()
