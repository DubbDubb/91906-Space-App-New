from tkinter.font import Font
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import random
import string
import ast

# Setup the main application window
root = Tk()
root.config(bg='grey', padx=100, pady=70)
root.title("App")
root.geometry('550x700+50+50')
root.resizable(False, False)

# Background image
background_image = PhotoImage(file=r"C:\Users\lutuz\Space App\Assets\background.png")
background_image_label = Label(root, image=background_image)
background_image_label.place(x=-120, y=-70)

# Create a white square to put everything in
whiteSquare = Label(root, bg="white", width=50, height=30)
whiteSquare.place(x=0, y=0)


def generate_temp_password():
    # Function to generate a temporary password
    temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    username = username_entry.get()

    # File path for the temporary passwords file
    file_path = r"C:\Users\lutuz\Space App\Data\temporarypasswords.txt"

    # Write the generated temporary password to the file
    with open(file_path, 'a') as file:
        file.write(f"{username}: {temp_password}\n")

    # Display the temporary password and copy it to the clipboard
    root.clipboard_clear()
    root.clipboard_append(temp_password)
    root.update()  # This is required on macOS to trigger clipboard update
    messagebox.showinfo("Temporary Password", f"Temporary password for {username}: {temp_password}\n\nThe password has been copied to the clipboard.")


# Create and place the widgets
label = tk.Label(root, text="Forgot Password?", font=('Microsoft Yahei UI light', 20), fg="#57a1f8", pady=10, bg="white")
label.pack(pady=15)

username_label = tk.Label(root, text="Username or Email:", font=('Microsoft Yahei UI light', 20), fg="#57a1f8", pady=10, bg="white")
username_label.pack(pady=15)

username_entry = tk.Entry(root, width=30, border=0, fg="#57a1f8")
username_entry.pack(pady=15)
username_line = Canvas(root, width=200, height=2.0, bg='black', highlightthickness=0)
username_line.place(x=75, y=220)

reset_button = tk.Button(root, text="Reset Password", command=generate_temp_password, font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)
reset_button.pack(pady=15)

# Previous page function
def previousPage():
    root.destroy()
    import Login


# Next page function
def previousPage1():
    root.destroy()
    import Register


# Already have account button
already_have_account_button = Button(root, text="Already Have an Account? Login!", command=previousPage, fg="black", bg="white", font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
already_have_account_button.place(x=70, y=300)

# Create account button
account_button = Button(root, text="Don't have an account? Create One!", command=previousPage1, fg="black", bg="white", font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
account_button.place(x=60, y=355)

root.mainloop()