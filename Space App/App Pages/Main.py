from tkinter import *
from tkinter import messagebox

# Define colors for light and dark modes
light_bg_color = 'white'
light_fg_color = 'black'
dark_bg_color = '#1a1a1a'
dark_fg_color = 'white'
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

#Function to enable dark mode
def toggle_dark_mode(): #Got some help from stack overflow
    global is_dark_mode
    if is_dark_mode:
        root.config(bg='white')
        planet_label.config(bg='white', fg="#57a1f8")
        planet2_label.config(bg='white', fg="#57a1f8")
        planet1_menu.config(bg='white', fg="#57a1f8")
        planet2_menu.config(bg='white', fg="#57a1f8")
        label_distance.config(bg='white', fg="#57a1f8")
        calculate_button.config(bg="#57a1f8")
        planet_calulator_title.config(bg='white', fg="#57a1f8")
        dark_mode_button.config(text="Dark Mode", bg="#57a1f8")
        logout_button.config(bg="#57a1f8")
        nextPage_button.config(bg="#57a1f8")
        is_dark_mode = False
    else:
        root.config(bg=dark_bg_color)
        planet_label.config(bg=dark_bg_color, fg=dark_fg_color)
        planet2_label.config(bg=dark_bg_color, fg=dark_fg_color)
        planet1_menu.config(bg=dark_bg_color, fg=dark_fg_color)
        planet2_menu.config(bg=dark_bg_color, fg=dark_fg_color)
        label_distance.config(bg=dark_bg_color, fg=dark_fg_color)
        calculate_button.config(bg=dark_button_color)
        logout_button.config(bg=dark_button_color)
        nextPage_button.config(bg=dark_button_color)
        planet_calulator_title.config(bg=dark_bg_color, fg=dark_fg_color)
        dark_mode_button.config(text="Light Mode", bg=dark_button_color)
        is_dark_mode = True

#next page function
def nextPage():
    """
    Navigate to the next page.
    """
    root.destroy()
    import Main3

# Function to log out and return to the login page
def log_out():
     """Log out and return to the login page."""
     response = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
     if response:
        root.destroy()
        import Login

#Function to calculate distance
def calculate_distance(): #Got help from stack overflow
    source_planet = planet1_var.get()
    target_planet = planet2_var.get()

    if source_planet in planet_distances and target_planet in planet_distances[source_planet]:
        distance = planet_distances[source_planet][target_planet]
        label_distance.config(text=f"Distance from {source_planet} to {target_planet} is {distance} million km")
    else:
        label_distance.config(text="Invalid planet selection.")
        label_distance.place(x=300, y=300)

# Create the main window
root = Tk()
root.geometry('800x500')
root.config(bg='white')
root.title("Planet Distance Calculator")

# Put an image in
image = PhotoImage(file="Assets/logo.png")
image = image.subsample(10)#got this line online it makes the image 10x10 pixels
image_label = Label(root, image=image, height=69, width=69)
image_label.place(x=580 ,y=50)

planet_label= Label(root, text="Pick your first planet", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
planet_label.place(x=100,y=150)

planet2_label= Label(root, text="Pick your second planet", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
planet2_label.place(x=100, y=250)

# Get the list of planet names from your dictionary keys
planet_names = list(planet_distances.keys())

# Create StringVar variables for the dropdown menus
planet1_var = StringVar()
planet2_var = StringVar()

planet_calulator_title = Label(root, text="Planet Distance Calculator", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
planet_calulator_title.place(x=80,y=50)

# Create a button to navigate to the previous planet
nextPage_button = Button(root, text="Next Page", command=nextPage, font=('Microsoft Yahei UI light', 16), bg="#57a1f8", fg="white", border=0)
nextPage_button.place(x=550, y=450)

# Create dropdown menus
planet1_menu = OptionMenu(root, planet1_var, *planet_names)
planet1_menu.config(font=('Microsoft Yahei UI light', 14), bg="white", fg="#57a1f8")
planet1_menu.place(x=600, y=150)

planet2_menu = OptionMenu(root, planet2_var, *planet_names)
planet2_menu.config(font=('Microsoft Yahei UI light', 14), bg="white", fg="#57a1f8")
planet2_menu.place(x=600, y=250)

label_distance = Label(root, text="", font=('Microsoft Yahei UI light', 16), bg="white", fg="#57a1f8")
label_distance.place(x=200, y=350)

calculate_button = Button(root, text="Calculate Distance", command=calculate_distance, font=('Microsoft Yahei UI light', 16), bg="#57a1f8", fg="white", border=0)
calculate_button.place(x=300, y=450)

# Create a variable to track dark mode state
is_dark_mode = False

# Log out button
logout_button = Button(root, text="Log Out", command=log_out, font=('Microsoft Yahei UI light', 16), bg="#57a1f8", fg="white", border=0)
# Log out button placement
logout_button.place(x=700,y=450)

# Create a button to toggle dark mode
dark_mode_button = Button(root, text="Dark Mode", command=toggle_dark_mode, font=('Microsoft Yahei UI light', 12), bg="#57a1f8", fg="white", border=0)
dark_mode_button.place(x=700, y=10)

# Start the main event loop
root.mainloop()
