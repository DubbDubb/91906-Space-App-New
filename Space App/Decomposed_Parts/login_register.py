import tkinter as tk
from tkinter import messagebox
import ast
import re

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.config(bg='black', padx=100, pady=70)
        self.root.title("App")
        self.root.geometry('1150x700+50+50')
        self.root.resizable(False, False)
        
        # Setimages
        self.show_image = tk.PhotoImage(file="Assets/show.png")
        self.hide_image = tk.PhotoImage(file="Assets/hide.png")

        # Set up the initial state of dark mode
        self.is_dark_mode = False

        # Dark mode color scheme
        self.dark_bg_color = '#1a1a1a'
        self.dark_fg_color = '#ffffff'
        self.dark_button_color = '#3f3f3f'
        self.dark_highlight_color = '#57a1f8'

        # String variables
        self.username = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_password = tk.StringVar()

        # Create a white square to put everything in
        self.whiteSquare = tk.Label(self.root, bg="white", width=50, height=35)
        self.whiteSquare.place(x=580, y=0)

        # ... other widget creation ...

        # Register button
        self.register_button = tk.Button(self.root, text="Register", command=self.register, font=('Microsoft Yahei UI light', 10), bg="#57a1f8", width=30, height=1, pady=7, fg='white', border=0)
        self.register_button.place(x=630, y=400)

        # Already have account button
        self.already_have_account_button = tk.Button(self.root, text="Already Have an Account? Login!", command=self.previousPage, fg="black", bg="white", font=('Microsoft Yahei UI light', 10, 'underline'), pady=10, border=0)
        self.already_have_account_button.place(x=640, y=450)

        # Hide and show button
        self.show_button = tk.Button(self.root, image=self.show_image, command=self.show, relief=tk.FLAT, activebackground='white', bd=0, background='white', width=100, height=100)
        self.show_button.place(x=830, y=220)

    # ... other methods ...

    def toggle_dark_mode(self):
        """Toggle dark mode."""
        if self.is_dark_mode:
            # Switch to light mode
            self.root.config(bg='white')
            self.whiteSquare.config(bg="white")
            # ... adjust other widget colors ...
            self.is_dark_mode = False
        else:
            # Switch to dark mode
            self.root.config(bg=self.dark_bg_color)
            self.whiteSquare.config(bg=self.dark_bg_color)
            # ... adjust other widget colors ...
            self.is_dark_mode = True

    def register(self):
        """Handle the registration process."""
        username_val = self.username.get()
        password_val = self.password.get()
        email_val = self.email.get()
        confirm_password_val = self.confirm_password.get()

        # ... rest of the registration logic ...

    def previousPage(self):
        """Switch back to the login page."""
        self.root.destroy()
        import Login

    def show(self):
        """Show the password."""
        hide_button = tk.Button(self.root, image=self.hide_image, command=self.hide, relief=tk.FLAT, activebackground="white", bd=0, background='white')
        hide_button.place(x=867, y=257)
        self.password_entry.config(show='')
        self.confirm_password_entry.config(show='')

    def hide(self):
        """Hide the password."""
        show_button = tk.Button(self.root, image=self.show_image, command=self.show, relief=tk.FLAT, activebackground='white', bd=0, background='white')
        show_button.place(x=867, y=257)
        self.password_entry.config(show='*')
        self.confirm_password_entry.config(show='*')

def main():
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
