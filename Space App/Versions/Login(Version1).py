from tkinter import *
from tkinter import messagebox
import ast

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1300x700")
        self.root.config(bg="black")

        self.centerframe = Frame(root, bg='white')
        self.centerframe.pack(anchor='center', expand=True)

        self.show_login_page()

    def show_login_page(self):
        self.login_image = PhotoImage(file="Assets/login.png")
        self.login_image_label = Label(self.centerframe, image=self.login_image)
        self.login_image_label.pack()

        self.username_label = Label(self.centerframe, text="Username:", font=("Microsoft Yahei UI light", 10), bg="white")
        self.username_label.pack(pady=5)
        self.username_entry = Entry(self.centerframe, font=("Microsoft Yahei UI light", 10))
        self.username_entry.pack(pady=5)

        self.password_label = Label(self.centerframe, text="Password:", font=("Microsoft Yahei UI light", 10), bg="white")
        self.password_label.pack(pady=5)
        self.password_entry = Entry(self.centerframe, font=("Microsoft Yahei UI light", 10), show="*")
        self.password_entry.pack(pady=5)

        self.login_button = Button(self.centerframe, text="Login", command=self.login, font=("Microsoft Yahei UI light", 10),
                                   bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open("datasheet.txt", "r") as file:
                data = file.read()
                user_data = ast.literal_eval(data)
                if username in user_data and user_data[username]['password'] == password:
                    messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                else:
                    messagebox.showerror("Login Failed", "Invalid username or password.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")

root = Tk()
app = LoginPage(root)
root.mainloop()
