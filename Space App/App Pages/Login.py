"""
Import Modules
"""
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
import ast

def login():
    """Function to handle the login process."""
    username = words1.get()
    password = words2.get()

    # Check if both username and password are empty
    if not username and not password:
        messagebox.showerror("Login Failed", "Please fill in both username and password fields.")
        return
    # Check if only one of the fields is empty
    elif not username:
        messagebox.showerror("Login Failed", "Please fill out the username field.")
        return
    elif not password:
        messagebox.showerror("Login Failed", "Please fill out the password field.")
        return

    # File path
    file_path = r"C:\Users\lutuz\Space App\Data\datasheet.txt"

    # Read data from the text file
    with open(file_path, 'r') as file:
        data = file.read()
        data = ast.literal_eval(data)

    # Check if the username exists
    if username in data:
        user_data = data[username]
        if 'temp_password' in user_data and user_data['temp_password'] == password:
            # If the user logs in with a temporary password, prompt them to create a new password
            root.destroy()
        elif 'password' in user_data and user_data['password'] == password:
            # If the user logs in with their actual password, proceed to the main page
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            root.destroy()
            import Main
        else:
            messagebox.showerror("Login Failed", "Invalid password")
    else:
        messagebox.showerror("Login Failed", "Invalid username")

def nextPage1():
    """Function to switch to the "Forgot" page."""
    root.destroy()
    import Forgot

def nextPage2():
    """Function to switch to the "Main" page."""
    root.destroy()
    import Main

def show():
    """Function to show the password."""
    show_button = Button(root, image=show_image, command=hide, relief=FLAT, activebackground="white", bd=0,
                         background='white')
    show_button.place(x=710, y=244)
    words2_entry.config(show='')

def hide():
    """Function to hide the password."""
    hide_button = Button(root, image=hide_image, command=show, relief=FLAT, activebackground='white', bd=0,
                         background='white')
    hide_button.place(x=710, y=244)
    words2_entry.config(show='*')


# Setup the main application window
root = Tk()
root.config(bg='black', padx=100, pady=70)
root.title("Login Page")
root.geometry('1300x700+50+50')
root.resizable(False, False)

# Background image
background_image = PhotoImage(file="Assets/background.png")
background_image_label = Label(root, image=background_image)
background_image_label.place(x=-110, y=-70)

# Create a white square to put everything in
whiteSquare = Label(root, bg="white", width=150, height=35)
whiteSquare.place(x=0, y=0)

# Create the center frame to align the content in the middle when maximized
centerframe = Frame(root, bg='white')
centerframe.pack(anchor='center', expand=True)

# String variable for the username entry
words1 = StringVar()

# Create frames
frame = Frame(root, width=350, height=350, bg="white")
Frame(frame, width=295, height=2, bg="black")

frame1 = Frame(centerframe, bg='white')
frame1.grid(row=1, column=15)

# Username label
label1 = Label(frame1, text="Sign In", font=('Microsoft Yahei UI light', 15), bg="white", fg="#57a1f8", pady=10)
label1.grid(row=0, column=3, padx=10)

# Username entry
words_entry = Entry(frame1, textvariable=words1, fg='black', bg="white", font=('Microsoft Yahei UI light', 10),
                   highlightthickness=0, relief=FLAT)
words_entry.grid(row=7, column=3, padx=10, pady=10)
words_line = Canvas(frame1, width=150, height=2.0, bg='black', highlightthickness=0)
words_line.grid(row=9, column=3)

# Login label
login_label = Label(frame1, text="Username", font=('Microsoft Yahei UI light', 10), bg="white", fg="black", pady=10)
login_label.grid(row=7, column=0)

# More frames
frame5 = Frame(centerframe, bg='white')
frame5.grid(row=0, column=0)

# Setimages
show_image = PhotoImage(file="Assets/show.png")
hide_image = PhotoImage(file="Assets/hide.png")

# Image labels
login_image = PhotoImage(file="Assets/login.png")
login_image_label = Label(root, image=login_image, height=325, width=390)
login_image_label.place(x=0, y=90)

image = PhotoImage(file="Assets/logo.png")
image = image.subsample(10)
image_label = Label(frame1, image=image, height=69, width=69)
image_label.grid(row=0, column=0)

# Second StringVar to store the password
words2 = StringVar()

frame2 = Frame(centerframe, bg='white')
frame2.grid(row=9, column=15)

# Password label
password_label = Label(frame2, text="Password", font=('Microsoft Yahei UI light', 10), fg="black", bg="white",
                       pady=5)
password_label.grid(row=7, column=10)

# Password entry
words2_entry = Entry(frame2, textvariable=words2, show="*", fg='black', bg="white",
                     font=('Microsoft Yahei UI light', 10), highlightthickness=0, relief=FLAT)
words2_entry.grid(row=7, column=34, padx=10, pady=13)
words2_line = Canvas(frame2, width=150, height=2.0, bg='black', highlightthickness=0)
words2_line.grid(row=9, column=34)

#3rd Frame
frame3 = Frame(centerframe, bg='white')
frame3.grid(row=23, column=15)

#4th Frame
frame4 = Frame(centerframe, bg='white')
frame4.grid(row=14, column=15)

# Check button to check if they wish to stay logged in
keep_logged_in = IntVar()

# Login button
login_button = Button(frame4, text="Login", command=login, font=('Microsoft Yahei UI light', 10), bg="#57a1f8",
                      width=30, height=1, pady=7, fg='white', border=0)
login_button.grid(row=10, column=5, pady=10, padx=5)

# Create account button
account_button = Button(frame3, text="Don't have an account? Create One!", command=nextPage1, fg="black", bg="white",
                        font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
account_button.grid(row=9, column=0)

# Forgot button
forgot_button = Button(frame3, text="Forgot Username or Password?", command=nextPage1,
                       font=('Microsoft Yahei UI light', 10, 'underline'), fg="black", bg="white", pady=10, border=0)
forgot_button.grid(row=10, column=0)


# Hide and show button
show_button = Button(root, image=show_image, command=show, relief=FLAT, activebackground='white', bd=0,
                     background='white', width=100, height=100)
show_button.place(x=673, y=207)

# Runs GUI Mainloop
root.mainloop()