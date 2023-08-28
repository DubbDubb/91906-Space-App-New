"""
Import Modules
"""
from tkinter.font import Font
from  tkinter import *
from  tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import ast
import re  # Add this line to import the 're' module for email validation

# Function to check if the username is the default text
def is_default_username(username):
    """Check if the username is the default text."""
    default_text = "Username"
    return username == default_text

def on_enter(event):
    """Event handler for when the mouse enters the entry widget."""
    if username_entry.get() == 'Username':
        # Clear the default 'Username' text
        username_entry.delete(0, tk.END)
        # Hide the username entry temporarily
        username_entry.pack_forget()
        # Show the email entry in its place
        email_entry.place(x=690, y=190)
        # Hide the username entry temporarily
        username_entry.pack_forget()
        # Show the email entry in its place
        email_entry.place(x=690, y=190)
        

def delete(event):
    """Event handler for when the mouse enters the entry widget."""
    if email_entry.get() == 'Email':
        # Clear the default 'Email' text
        email_entry.delete(0, tk.END)
        # Hide the email entry temporarily
        email_entry.pack_forget()
        # Show the username entry in its place
        username_entry.place(x=690, y=120)
        # Hide the email entry temporarily
        email_entry.pack_forget()
        # Show the username entry in its place
        username_entry.place(x=690, y=120)
        

def press(event):
    """Event handler for when a key is pressed in the password entry widget."""
    if password_entry.get() == 'Password':
        # Clear the default 'Password' text
        password_entry.delete(0, tk.END)
        # Show the actual password characters
        password_entry.config(show="*")

def click(event):
    """Event handler for when a key is pressed in the confirm password entry widget."""
    if confirm_password_entry.get() == 'Confirm Password':
        # Clear the default 'Confirm Password' text
        confirm_password_entry.delete(0, tk.END)
        # Show the actual password characters
        confirm_password_entry.config(show="*")
        

#previous page function
def previousPage():
    """Switch back to the login page."""
    root.destroy()
    import Login

#Function to run the hide password button
def show():
    """Show the password."""
    show_button = Button(root, image=show_image ,command=hide, relief=FLAT, activebackground="white", bd=0, background='white')
    show_button.place(x=867, y=257)
    password_entry.config(show='')
    confirm_password_entry.config(show='')

def set_entry_bg_color(color):
    """
    Set the background color of the entry widgets to the specified color.

    Parameters:
    color (str): The background color to set for the entry widgets.

    Returns:
    None
    """
    entry_bg_color = color
    username_entry.config(bg=entry_bg_color)
    email_entry.config(bg=entry_bg_color)
    password_entry.config(bg=entry_bg_color)
    confirm_password_entry.config(bg=entry_bg_color)

def set_canvas_line_color(color):
    """
    Set the color of the canvas lines to the specified color.

    Parameters:
    color (str): The color to set for the canvas lines.

    Returns:
    None
    """
    username_line.config(bg=color)
    email_line.config(bg=color)
    password_line.config(bg=color)
    confirm_password_line.config(bg=color)

# Toggle dark mode function
def toggle_dark_mode():
    """Toggle dark mode."""
    global is_dark_mode
    if is_dark_mode:
        # Switch to light mode
        root.config(bg='white')
        whiteSquare.config(bg="white")
        Register_label.config(bg="white", fg="#57a1f8")
        show_button.config(bg='white', activebackground='white')
        dark_mode_button.config(bg=dark_highlight_color, fg=dark_fg_color)
        set_entry_bg_color('white')  # Set entry background to white
        set_canvas_line_color('black')  # Set canvas lines to black
        already_have_account_button.config(bg="white", fg="black")  # Set background to white and text to black
        is_dark_mode = False
    else:
        # Switch to dark mode
        root.config(bg='black')
        whiteSquare.config(bg='black')
        Register_label.config(bg='black', fg='white')
        show_button.config(bg='black', activebackground='black')
        dark_mode_button.config(bg=dark_highlight_color, fg=dark_fg_color)
        set_entry_bg_color('black')  # Set entry background to black
        set_canvas_line_color('white')  # Set canvas lines to white
        already_have_account_button.config(bg="black", fg="white")  # Set background to black and text to white
        is_dark_mode = True

# Function to check if the email exists in the data file
def is_existing_email(email):
    """Check if the email exists in the data file."""
    file_path = r"C:\Users\lutuz\Space App\Data\datasheet.txt"
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                existing_data = ast.literal_eval(data)
                for user_data in existing_data.values():
                    if 'email' in user_data and user_data['email'] == email:
                        return True
    except (FileNotFoundError, ValueError):
        pass
    return False

def hide():
    """Hide the password."""
    hide_button = Button(root, image=hide_image ,command=show, relief=FLAT, activebackground='white', bd=0, background='white')
    hide_button.place(x=867, y=257)
    password_entry.config(show='*')
    confirm_password_entry.config(show='*')

# Function to handle the insertion of default text when entry gains focus
def on_focus_in(default_text, entry_widget, line_widget):
    """Handle the insertion of default text when entry gains focus."""
    if entry_widget.get() == default_text:
        entry_widget.delete(0, END)
    line_widget.config(bg="#57a1f8")

# Function to handle the deletion of default text when entry loses focus
def on_focus_out(default_text, entry_widget, line_widget):
    """Handle the deletion of default text when entry loses focus."""
    if entry_widget.get() == "":
        entry_widget.insert(0, default_text)
    line_widget.config(bg="black")

# Register function with email validation
def register():
    """Handle the registration process."""
    username_val = username_entry.get()
    password_val = password_entry.get()
    email_val = email_entry.get()
    confirm_password_val = confirm_password_entry.get()

    # Check if any of the fields are empty
    if not username_val or not email_val or not password_val or not confirm_password_val:
        messagebox.showerror("Registration Failed", "Please fill in all the fields")
        return

    # Check if the password and confirm password match
    if password_val != confirm_password_val:
        messagebox.showerror("Registration Failed", "Passwords do not match")
        return

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_val):
        messagebox.showerror("Registration Failed", "Invalid email format. Please enter a valid email address such as @gmail.com.")
        return

    # Check if the email already exists
    if is_existing_email(email_val):
        messagebox.showerror("Registration Failed", "Email already exists. Please use a different email.")
        return

    # File path
    file_path = r"C:\Users\lutuz\Space App\Data\datasheet.txt"

    # Create a dictionary to store the user data
    user_data = {
        'username': username_val,
        'password': password_val,
        'email': email_val
    }

    # Read existing data from the text file
    with open(file_path, 'r') as file:
        data = file.read()
        if data:
            existing_data = ast.literal_eval(data)
        else:
            existing_data = {}

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

# Function to check if the email exists in the data file
def is_existing_email(email):
    file_path = r"C:\Users\lutuz\Space App\Data\datasheet.txt"
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if data:
                existing_data = ast.literal_eval(data)
                for user_data in existing_data.values():
                    if 'email' in user_data and user_data['email'] == email:
                        return True
    except (FileNotFoundError, ValueError):
        pass
    return False 

# Set up the initial state of dark mode
is_dark_mode = False

# Dark mode color scheme
dark_bg_color = '#1a1a1a'
dark_fg_color = '#ffffff'
dark_button_color = '#3f3f3f'
dark_highlight_color = '#57a1f8'

#setup
root = Tk()
root.config(bg='black', padx=100, pady=70)
root.title("App")
root.geometry('1150x700+50+50')
root.resizable(False,False)

#Background image
background_image = PhotoImage(file="Assets/background.png")
background_image_label = Label(root, image=background_image)
background_image_label.place(x=-120, y=-70)

#set images   
show_image = PhotoImage(file="Assets/show.png")
hide_image = PhotoImage(file="Assets/hide.png")

#create a white square to put everything in
whiteSquare = Label(root,bg="white",width=50,height=35)
whiteSquare.place(x=580,y=0)

#string variable for my username entry
username = StringVar()
email = StringVar()
password =StringVar()
confirm_password = StringVar()

#username label
Register_label = Label(root, text="Register", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8", pady=10)
Register_label.place(x=700,y=25)

#Image labels
username_image = PhotoImage(file="Assets/username.png")
username_image_label = Label(root, image=username_image, height=30, width=30)
username_image_label.place(x=640, y=120)

#Register Image 
register_image = PhotoImage(file="Assets/register.png")
register_image_label = Label(root, image=register_image)
register_image_label.place(x=-50, y=-40)

#Email Image
email_image = PhotoImage(file="Assets/email.png")
email_image_label = Label(root, image=email_image, height=30, width=30)
email_image_label.place(x=640, y=185)

# Dark mode toggle button
dark_mode_button = Button(root, text="Dark Mode", command=toggle_dark_mode, font=('Microsoft Yahei UI light', 10), bg=dark_button_color, fg='white', border=0)
dark_mode_button.place(x=710, y=500)

password_image = PhotoImage(file="Assets/password.png")
password_image_label = Label(root, image=password_image, height=30, width=30)
password_image_label.place(x=640, y=255)

# Create username entries with default text
username_entry = Entry(root, textvariable=username, font=('Microsoft Yahei UI light', 13), bg="white", fg="#57a1f8", relief=FLAT)
username_entry.place(x=690, y=120)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', lambda event: on_focus_in('Username', username_entry, username_line))
username_entry.bind('<FocusOut>', lambda event: on_focus_out('Username', username_entry, username_line))
username_line = Canvas(root, width=150, height=2.0, bg='black', highlightthickness=0)
username_line.place(x=685, y=150)

#Creates email entries with default text
email_entry = Entry(root, textvariable=email, font=('Microsoft Yahei UI light', 13), bg="white", fg="#57a1f8", relief=FLAT)
email_entry.place(x=692, y=190)
email_entry.insert(0, 'Email')
email_entry.bind('<FocusIn>', lambda event: on_focus_in('Email', email_entry, email_line))
email_entry.bind('<FocusOut>', lambda event: on_focus_out('Email', email_entry, email_line))
email_line = Canvas(root, width=150, height=2.0, bg='black', highlightthickness=0)
email_line.place(x=685, y=220)

#Creates password entries with default text
password_entry = Entry(root, textvariable=password, show='', font=('Microsoft Yahei UI light', 13), bg="white", fg="#57a1f8", relief=FLAT)
password_entry.place(x=692, y=260)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', lambda event: on_focus_in('Password', password_entry, password_line))
password_entry.bind('<FocusOut>', lambda event: on_focus_out('Password', password_entry, password_line))
password_line = Canvas(root, width=150, height=2.0, bg='black', highlightthickness=0)
password_line.place(x=685, y=290)

#Creates confirm password entries with default text
confirm_password_entry = Entry(root, textvariable=confirm_password, show='', font=('Microsoft Yahei UI light', 13), bg="white", fg="#57a1f8", relief=FLAT)
confirm_password_entry.place(x=685, y=330)
confirm_password_entry.insert(0, 'Confirm Password')
confirm_password_entry.bind('<FocusIn>', lambda event: on_focus_in('Confirm Password', confirm_password_entry, confirm_password_line))
confirm_password_entry.bind('<FocusOut>', lambda event: on_focus_out('Confirm Password', confirm_password_entry, confirm_password_line))
confirm_password_line = Canvas(root, width=150, height=2.0, bg='black', highlightthickness=0)
confirm_password_line.place(x=685, y=360)

#register Button
register_button = Button(root, text="Register",command=register, font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)
register_button.place(x=630,y=400)

#Already have account button
already_have_account_button = Button(root, text="Already Have an Account? Login!",command=previousPage , fg="black", bg="white",font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
already_have_account_button.place(x=640, y=450)

#Hide and show button
show_button = Button(root, image=show_image, command=show, relief=FLAT, activebackground='white', bd=0, background='white', width=100, height=100)
show_button.place(x=830, y=220)

#Run the program
root.mainloop()   