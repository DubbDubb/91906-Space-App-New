from tkinter import *
from tkinter import messagebox
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
root.config(bg='#f5f5f5')
root.title("Register")
root.geometry('400x400+50+50')
root.resizable(False, False)

# Create a top frame for the title
title_frame = Frame(root, bg='#57a1f8')
title_frame.pack(fill=BOTH)

# Title label
title_label = Label(title_frame, text="Create an Account", font=('Arial', 20), bg='#57a1f8', fg='white')
title_label.pack(pady=20)

# Create a middle frame for the entry widgets
middle_frame = Frame(root, bg='#f5f5f5')
middle_frame.pack(fill=BOTH)

# Create username and password entry widgets
username = StringVar()
password = StringVar()

username_label = Label(middle_frame, text="Username", font=('Arial', 14), bg='#f5f5f5')
username_label.pack(pady=5, padx=10, anchor="w")

username_entry = Entry(middle_frame, textvariable=username, font=('Arial', 14), relief=FLAT)
username_entry.pack(fill=X, padx=10, pady=5)

password_label = Label(middle_frame, text="Password", font=('Arial', 14), bg='#f5f5f5')
password_label.pack(pady=5, padx=10, anchor="w")

password_entry = Entry(middle_frame, textvariable=password, show='*', font=('Arial', 14), relief=FLAT)
password_entry.pack(fill=X, padx=10, pady=5)

# Create register button
register_button = Button(root, text="Register", command=register, font=('Arial', 14), bg="#57a1f8", fg='white', relief=FLAT)
register_button.pack(pady=20)

# Create a bottom frame for additional options
bottom_frame = Frame(root, bg='#f5f5f5')
bottom_frame.pack(fill=BOTH)

# Already have an account label
already_have_label = Label(bottom_frame, text="Already have an account?", font=('Arial', 12), bg='#f5f5f5')
already_have_label.pack(pady=10)

# Login button
login_button = Button(bottom_frame, text="Log in", command=lambda: root.destroy(), font=('Arial', 12), bg='white', fg='#57a1f8', relief=FLAT)
login_button.pack()

# Run the program
root.mainloop()
