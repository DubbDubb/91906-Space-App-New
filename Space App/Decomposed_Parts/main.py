"""
Import Modules
"""
from tkinter import *
from tkinter import messagebox

# Dark mode color scheme
dark_bg_color = '#1a1a1a'
dark_fg_color = '#ffffff'
dark_button_color = '#3f3f3f'
dark_highlight_color = '#57a1f8'

# Dictionary to store planet distances
planet_distances = {
    "Mercury": {
        "Mercury": 0.0,
        "Venus": 48.0,
        "Earth": 91.7,
        "Mars": 178.4,
        "Jupiter": 588.8,
        "Saturn": 1214.3,
        "Uranus": 2536.1,
        "Neptune": 3928.4,
    },
    "Venus": {
        "Mercury": 48.0,
        "Venus": 0.0,
        "Earth": 43.7,
        "Mars": 130.4,
        "Jupiter": 540.8,
        "Saturn": 1166.3,
        "Uranus": 2488.1,
        "Neptune": 3880.4,
    },
    "Earth": {
        "Mercury": 91.7,
        "Venus": 43.7,
        "Earth": 0.0,
        "Mars": 86.7,
        "Jupiter": 497.1,
        "Saturn": 1122.6,
        "Uranus": 2444.4,
        "Neptune": 3836.7,
    },
    "Mars": {
        "Mercury": 178.4,
        "Venus": 130.4,
        "Earth": 86.7,
        "Mars": 0.0,
        "Jupiter": 410.4,
        "Saturn": 1035.9,
        "Uranus": 2357.7,
        "Neptune": 3750.0,
    },
    "Jupiter": {
        "Mercury": 588.8,
        "Venus": 540.8,
        "Earth": 497.1,
        "Mars": 410.4,
        "Jupiter": 0.0,
        "Saturn": 625.5,
        "Uranus": 1947.3,
        "Neptune": 3340.7,
    },
    "Saturn": {
        "Mercury": 1214.3,
        "Venus": 1166.3,
        "Earth": 1122.6,
        "Mars": 1035.9,
        "Jupiter": 625.5,
        "Saturn": 0.0,
        "Uranus": 1322.8,
        "Neptune": 2716.2,
    },
    "Uranus": {
        "Mercury": 2536.1,
        "Venus": 2488.1,
        "Earth": 2444.4,
        "Mars": 2357.7,
        "Jupiter": 1947.3,
        "Saturn": 1322.8,
        "Uranus": 0.0,
        "Neptune": 1393.4,
    },
    "Neptune": {
        "Mercury": 3928.4,
        "Venus": 3880.4,
        "Earth": 3836.7,
        "Mars": 3750.0,
        "Jupiter": 3340.7,
        "Saturn": 2716.2,
        "Uranus": 1393.4,
        "Neptune": 0.0,
    },
}

# Function to log out and return to the login page
def log_out():
     """
    Log out and return to the login page.
    """
     response = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
     if response:
        root.destroy()
        import Login

# Function to toggle dark mode
def toggle_dark_mode():
    """
    Toggle dark mode.

    This function switches between light mode and dark mode by changing the color scheme of the UI elements.
    """
    global is_dark_mode
    if is_dark_mode:
        # Light mode theme
        root.config(bg='white')
        label_title.config(bg='white', fg="#57a1f8")
        label_source.config(bg='white', fg="#57a1f8")
        label_target.config(bg='white', fg="#57a1f8")
        label_distance.config(bg='white', fg="#57a1f8")
        dropdown_source.config(bg='white', fg="#57a1f8", highlightbackground="gray")
        dropdown_target.config(bg='white', fg="#57a1f8", highlightbackground="gray")
        logout_button.config(bg="#57a1f8")
        dark_mode_button.config(bg="#57a1f8")
        button_calculate.config(bg="#57a1f8", fg="white")
        next_button.config(bg="#57a1f8", fg="white")
        is_dark_mode = False
    else:
        # Dark mode theme
        root.config(bg=dark_bg_color)
        label_title.config(bg=dark_bg_color, fg=dark_fg_color)
        label_source.config(bg=dark_bg_color, fg=dark_fg_color)
        label_target.config(bg=dark_bg_color, fg=dark_fg_color)
        label_distance.config(bg=dark_bg_color, fg=dark_fg_color)
        dropdown_source.config(bg=dark_bg_color, fg=dark_fg_color, highlightbackground=dark_fg_color)
        dropdown_target.config(bg=dark_bg_color, fg=dark_fg_color, highlightbackground=dark_fg_color)
        logout_button.config(bg=dark_button_color)
        dark_mode_button.config(bg=dark_button_color)
        button_calculate.config(bg=dark_button_color, fg="white")
        next_button.config(bg=dark_button_color, fg="white")
        is_dark_mode = True

# Function to calculate the distance
def calculate_distance():
    """
    Calculate the distance between source and target planets.

    This function calculates the distance between the selected source and target planets.
    """
    source_planet = source_planet_var.get()
    target_planet = target_planet_var.get()
    if source_planet in planet_distances and target_planet in planet_distances[source_planet]:
        distance = planet_distances[source_planet][target_planet]
        label_distance.config(text=f"Distance from {source_planet} to {target_planet}: {distance} million km")
    else:
        messagebox.showerror("Error", "Invalid planet selection.")

#next page function
def nextPage():
    """
    Navigate to the next page.
    """
    root.destroy()
    import Main2

# Create the main window
root = Tk()
root.geometry('800x500')
root.config(bg='white')
root.title("Planet Distance Calculator")

# Put an image in
image = PhotoImage(file="Assets/logo.png")
image = image.subsample(10)
image_label = Label(root, image=image, height=69, width=69)
image_label.place(x=580 ,y=50)

# Log out button
logout_button = Button(root, text="Log Out", command=log_out, font=('Microsoft Yahei UI light', 20), bg="#57a1f8", fg="white", border=0)
# Log out button placement
logout_button.place(x=180, y=378)

# Dark mode toggle button
dark_mode_button = Button(root, text="Toggle Dark Mode", command=toggle_dark_mode, font=('Microsoft Yahei UI light', 12), bg="#57a1f8", fg="white", border=0)
dark_mode_button.place(x=20, y=390)

# Set the default theme to light mode
is_dark_mode = False

# Create labels and dropdowns
label_title = Label(root, text="Planet Distance Calculator", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
label_source = Label(root, text="Source Planet:", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
label_target = Label(root, text="Target Planet:", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
source_planet_var = StringVar()
target_planet_var = StringVar()
dropdown_source = OptionMenu(root, source_planet_var, *planet_distances.keys())
dropdown_target = OptionMenu(root, target_planet_var, *planet_distances.keys())
label_distance = Label(root, text="Distance:", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")

dropdown_source.config(
    font=("Arial", 12),  # Set the font
    width=5,  # Set the width
    bg="white",  # Set the background color
    fg="white",  # Set the text color
    relief="solid",  # Set the border style
    highlightthickness=1,  # Set the border thickness
    highlightbackground="gray",  # Set the border color
    padx=10,  # Set horizontal padding
    pady=5  # Set vertical padding
)

dropdown_target.config(
    font=("Arial", 12),  # Set the font
    width=5,  # Set the width
    bg="white",  # Set the background color
    fg="white",  # Set the text color
    relief="solid",  # Set the border style
    highlightthickness=1,  # Set the border thickness
    highlightbackground="gray",  # Set the border color
    padx=10,  # Set horizontal padding
    pady=5  # Set vertical padding
)

# Configure the OptionMenus
dropdown_source.config(font=('Microsoft Yahei UI light', 14), bg="white", fg="#57a1f8")
dropdown_target.config(font=('Microsoft Yahei UI light', 14), bg="white", fg="#57a1f8")
dropdown_source["menu"].config(font=('Microsoft Yahei UI light', 14), bg="white", fg="#57a1f8")
dropdown_target["menu"].config(font=('Microsoft Yahei UI light', 14), bg="white", fg="#57a1f8")

# Create calculate button
button_calculate = Button(root, text="Calculate", command=calculate_distance , font=('Microsoft Yahei UI light', 20), bg="#57a1f8", fg="white", border=0)

# Next page button
next_button = Button(root, text="Next Page", command=nextPage, font=('Microsoft Yahei UI light', 20), bg="#57a1f8", fg="white", border=0)
next_button.place(x=500, y=378)

# Set the layout using grid
label_title.grid(row=0, column=0, columnspan=2, pady=10)
label_source.grid(row=1, column=0)
dropdown_source.grid(row=1, column=1)
label_target.grid(row=2, column=0)
dropdown_target.grid(row=2, column=1)
label_distance.grid(row=3, column=0, columnspan=2, pady=10)

button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Center the calculator vertically and horizontally
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the main event loop
root.mainloop()