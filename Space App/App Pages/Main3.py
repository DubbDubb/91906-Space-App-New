"""
Import Modules
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re
from tkinter import StringVar
from tkinter import messagebox

# Planet data
planet_data = [
    {
        'name': 'Mercury',
        'radius': 24.4,
        'distance': 57.9,
        'info': 'Mercury is the smallest planet in the Solar System and the closest to the Sun. It\'s a small World. Mercury is the smallest planet in our solar system – only slightly larger than Earth\'s Moon.',
        'details': 'Mercury is a rocky planet with no atmosphere. It has a heavily cratered surface and extreme temperature variations.',
    },
    {
        'name': 'Venus',
        'radius': 60.5,
        'distance': 108.2,
        'info': 'Venus is the second planet from the Sun and is known for its thick atmosphere and hot surface temperature. Even though Mercury is closer to the Sun, Venus is the hottest planet in our solar system. Its thick atmosphere is full of the greenhouse gas carbon dioxide, and it has clouds of sulfuric acid.',
        'details': 'Venus has a dense atmosphere consisting mainly of carbon dioxide. It has a runaway greenhouse effect, making it the hottest planet in our solar system with surface temperatures hot enough to melt lead.',
    },
    {
        'name': 'Earth',
        'radius': 63.7,
        'distance': 149.6,
        'info': 'Earth is the third planet from the Sun and is the only known celestial body to support life. Earth is the biggest of the four planets closest to the Sun, all of which are made of rock and metal',
        'details': 'Earth is the only planet known to support life. It has a diverse ecosystem with a wide range of environments and habitats. The presence of liquid water, an atmosphere rich in oxygen, and a suitable range of temperatures make Earth uniquely suited for life as we know it.',
    },
    {
        'name': 'Mars',
        'radius': 33.9,
        'distance': 227.9,
        'info': 'Mars is the fourth planet from the Sun and is often referred to as the "Red Planet" due to its reddish appearance. It\'s red because of rusty iron in the ground. Like Earth, Mars has seasons, polar ice caps, volcanoes, canyons, and weather. It has a very thin atmosphere made of carbon dioxide, nitrogen, and argon.',
        'details': 'Mars is a terrestrial planet with a thin atmosphere. It has the largest volcano, Olympus Mons, and the longest canyon, Valles Marineris, in the solar system. Mars also has polar ice caps made of water and carbon dioxide.',
    },
    {
        'name': 'Jupiter',
        'radius': 699.1,
        'distance': 778.5,
        'info': 'Jupiter is the largest planet in the Solar System and is known for its iconic Great Red Spot. Jupiter has rings, but they\'re too faint to see very well and Jupiter has 80 moons.',
        'details': 'Jupiter is a gas giant composed mostly of hydrogen and helium. It is the largest planet in our solar system and has a strong magnetic field. Jupiter\'s Great Red Spot is a giant storm that has been raging for over 300 years.',
    },
    {
        'name': 'Saturn',
        'radius': 582.3,
        'distance': 1433.5,
        'info': 'Saturn is the second-largest planet in the Solar System and is known for its beautiful ring system. It has the brightest, most massive, and most complex ring system of any planet.',
        'details': 'Saturn is a gas giant with prominent rings made of ice particles and dust. It is known for its beautiful ring system, which is made up of thousands of individual rings. Saturn has at least 82 moons.',
    },
    {
        'name': 'Uranus',
        'radius': 253.6,
        'distance': 2872.5,
        'info': 'Uranus is the seventh planet from the Sun and is known for its unique sideways rotation. It is often referred to as an "ice giant" because it is made up mostly of icy materials.',
        'details': 'Uranus is an ice giant with a tilted axis of rotation. It is composed mostly of hydrogen and helium, with small amounts of methane giving it a blue-green appearance. Uranus has a unique rotation axis that is tilted sideways compared to other planets.',
    },
    {
        'name': 'Neptune',
        'radius': 246.2,
        'distance': 4495.1,
        'info': 'Neptune is the eighth planet from the Sun and is known for its deep blue color. It is the farthest planet from the Sun in our solar system.',
        'details': 'Neptune is an ice giant with a deep blue color. It has a dynamic atmosphere with large storms, including the Great Dark Spot, a giant storm system similar to Jupiter\'s Great Red Spot. Neptune has 14 known moons.',
    },
    {
        'name': 'Pluto',
        'radius': 11.6,
        'distance': 5906.4,
        'info': 'Pluto was formerly classified as the ninth planet in our Solar System, but it is now considered a dwarf planet. It is part of the Kuiper Belt, a region of icy bodies beyond the orbit of Neptune.',
        'details': 'Pluto is a dwarf planet located in the Kuiper Belt, a region of the solar system beyond the orbit of Neptune. It is primarily composed of rock and ice. Pluto has a highly elliptical orbit that takes it closer to the Sun than Neptune for a portion of its orbit.',
    },
]

# Image paths
image_paths = [
    "Assets/Mercury.jpg",
    "Assets/Venus.jpg",
    "Assets/Earth.jpg",
    "Assets/Mars.jpg",
    "Assets/Jupiter.jpg",
    "Assets/Saturn.jpg",
    "Assets/Uranus.jpg",
    "Assets/Neptune.jpg",
    "Assets/Pluto.jpg",
]

current_planet_index = 0  # Index of the current planet being viewed

# Function to display the current planet information
def display_planet_info():#Got help from stack overflow
    """Display the information of the current planet."""
    planet = planet_data[current_planet_index]
    info_text.set(planet['info'])
    details_text.set(planet['details'])

# Function to display the current planet image
def display_planet_image():
    """Display the image of the current planet."""
    image_path = image_paths[current_planet_index]
    image = Image.open(image_path)
    image.thumbnail((300, 200))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# Variable to track the state of details display
details_visible = False

# Function to show or hide the details based on the current state
def show_details():#Got help from stack overflow
    """
    Show or hide the detailed information about the current planet.

    This function toggles the visibility of the detailed information about the current planet.
    If the details are currently visible, this function hides them; otherwise, it shows the details.
    """
    global details_visible
    if details_visible:
        details_label.pack_forget()  # Hide the details
        details_visible = False
    else:
        details_label.pack(pady=10)  # Show the details
        details_visible = True

# Function to navigate to the next planet
def next_planet():#Got help from stack overflow
    """
    Navigate to the next planet in the sequence.

    This function updates the current planet index to move to the next planet in the list.
    It displays the information and image of the new current planet.
    """
    global current_planet_index
    current_planet_index = (current_planet_index + 1) % len(planet_data)
    display_planet_info()
    display_planet_image()

# Function to navigate to the previous planet
def previous_planet():
    """
    Navigate to the previous planet in the sequence.

    This function updates the current planet index to move to the previous planet in the list.
    It displays the information and image of the new current planet.
    """
    global current_planet_index
    current_planet_index = (current_planet_index - 1) % len(planet_data)
    display_planet_info()
    display_planet_image()

# Function to log out and return to the login page
def log_out():
     """Log out and return to the login page."""
     response = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
     if response:
        window.destroy()
        import Login

# Function to navigate back to the previous page
def previousPage():
    """
    Navigate back to the previous page.

    This function is called when the user wants to return to the previous page from the current page.
    It destroys the current window and navigates to the main page. 
    """
    window.destroy()
    import Main

# Create the main window
window = tk.Tk()
window.title("Planet Explorer")
window.geometry("750x750")
window.configure(bg="black")  # Set the background color to black

# Create a frame for the planet information
info_frame = ttk.Frame(window)
info_frame.pack(pady=20)

# Create a variable to store the search entry
search_entry_var = tk.StringVar()

# Create a label to display the planet information
info_text = tk.StringVar()
info_label = ttk.Label(info_frame, textvariable=info_text, wraplength=400, font=("Arial", 12), foreground="white")  # Set text color to white
info_label.pack()

# Create a button to show additional details
show_details_button = ttk.Button(info_frame, text="Show Details", command=show_details, style="Black.TButton")
show_details_button.pack(pady=10)

# Create a label to display the additional details
details_text = tk.StringVar()
details_label = ttk.Label(info_frame, textvariable=details_text, wraplength=400, font=("Arial", 12), foreground="white")  # Set text color to white

# Log out button
logout_button = ttk.Button(window, text="Log Out", command=log_out, style="Black.TButton")
# Log out button placement
logout_button.place(x=60,y=425)

# Create a frame for the planet image
image_frame = ttk.Frame(window)
image_frame.pack(pady=20)

# Create a label to display the planet image
image_label = ttk.Label(image_frame)
image_label.pack()

# Create a frame for the navigation buttons
nav_frame = ttk.Frame(window)
nav_frame.pack(pady=20)

# Create a button to navigate to the previous planet
previous_button = ttk.Button(nav_frame, text="Previous", command=previous_planet, style="Black.TButton")
previous_button.grid(row=0, column=0, padx=10)

# Create a button to navigate to the next planet
next_button = ttk.Button(nav_frame, text="Next", command=next_planet, style="Black.TButton")
next_button.grid(row=0, column=5, padx=10)

# Create a spacer label to align the Previous Page button
spacer_label = ttk.Label(nav_frame, text="", width=15)
spacer_label.grid(row=0, column=1)

# Previous page button
previous_page_button = ttk.Button(nav_frame, text="Previous Page", command=previousPage, style="Black.TButton")
previous_page_button.grid(row=0, column=1, padx=10, columnspan=1)

# Create a frame for the search bar
search_frame = ttk.Frame(window)
search_frame.pack(pady=20)

# Create a variable to store the planet names
planet_names = [planet['name'] for planet in planet_data]

# Configure the style for different widgets
style = ttk.Style()
style.configure("Black.TButton", foreground="black")

# Set the background and foreground color for all elements
style.configure(".", background="black", foreground="white")

# Override the specific elements with different style options
style.configure("TButton", relief="flat")
style.map("TButton",
          background=[('active', 'gray')],
          foreground=[('active', 'white')]), ('!disabled', 'black')

# Display the initial planet information and image
display_planet_info()
display_planet_image()

# Start the Tkinter event loop
window.mainloop()
