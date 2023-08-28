import tkinter as tk
from tkinter import colorchooser, messagebox


class PlanetCreatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Planet Creator")
        
        self.planets = {}
        
        self.create_planet_page()
    
    def create_planet_page(self):
        self.clear_frame()
        
        self.name_label = tk.Label(self.root, text="Planet Name:", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root, font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.name_entry.pack()

        self.colour_label = tk.Label(self.root, text="Colour:", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.colour_label.pack()

        self.colour_entry = tk.Entry(self.root, font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.colour_entry.pack()

        self.distance_label = tk.Label(self.root, text="Distance from Sun:", font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.distance_label.pack()
        
        self.distance_entry = tk.Entry(self.root, font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.distance_entry.pack()
        
        self.create_button = tk.Button(self.root, text="Create Planet", command=self.validate_and_create, font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.create_button.pack()
        
        self.see_planets_button = tk.Button(self.root, text="See Planets", command=self.see_planets, font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        self.see_planets_button.pack()
    
    def validate_and_create(self):
        name = self.name_entry.get()
        distance = self.distance_entry.get()
        color = self.colour_entry.get()
        
        if not self.is_valid_color(color):
            messagebox.showerror("Error", "Invalid color. Please choose a valid color.")
            return
        
        if name and color and distance:
            self.planets[name] = {'distance': distance, 'color': color}
            self.name_entry.delete(0, tk.END)
            self.colour_entry.delete(0, tk.END)
            self.distance_entry.delete(0, tk.END)
            messagebox.showinfo("Planet Created", f"Planet {name} created with distance {distance}")
        else:
            messagebox.showerror("Error", "Please enter both name, color, and distance.")
    
    def is_valid_color(self, color):
        try:
            self.root.winfo_rgb(color)  # Try to get RGB value of the color
            return True
        except tk.TclError:
            return False
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def see_planets(self):
        self.clear_frame()
        
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=300)
        self.canvas.pack()
        
        x = 100
        y = 150
        for planet, planet_info in self.planets.items():
            color = planet_info['color']
            self.canvas.create_oval(x-30, y-30, x+30, y+30, fill=color, outline="black")  # Draw a planet circle
            self.canvas.create_text(x, y+40, text=planet, font=('Microsoft Yahei UI light', 12))
            x += 100
        
        back_button = tk.Button(self.root, text="Back to Creation", command=self.create_planet_page, font=('Microsoft Yahei UI light', 20), bg="white", fg="#57a1f8")
        back_button.pack()
    
    def start(self):
        self.create_planet_page()
        
        self.root.geometry('800x500')
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlanetCreatorGUI(root)
    app.start()
