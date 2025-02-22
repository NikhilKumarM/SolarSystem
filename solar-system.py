import tkinter as tk
import math

# Constants for the solar system
WIDTH, HEIGHT = 800, 800
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
SUN_RADIUS = 30
PLANETS = [
    {"name": "Mercury", "radius": 5, "distance": 50, "speed": 0.02, "color": "gray"},
    {"name": "Venus", "radius": 8, "distance": 80, "speed": 0.015, "color": "yellow"},
    {"name": "Earth", "radius": 10, "distance": 120, "speed": 0.01, "color": "blue"},
    {"name": "Mars", "radius": 7, "distance": 160, "speed": 0.008, "color": "red"},
    {"name": "Jupiter", "radius": 20, "distance": 220, "speed": 0.005, "color": "orange"},
    {"name": "Saturn", "radius": 18, "distance": 280, "speed": 0.003, "color": "goldenrod"},
    {"name": "Uranus", "radius": 15, "distance": 340, "speed": 0.002, "color": "lightblue"},
    {"name": "Neptune", "radius": 13, "distance": 400, "speed": 0.001, "color": "darkblue"}
]

class SolarSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System Simulation")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.sun = self.canvas.create_oval(
            CENTER_X - SUN_RADIUS, CENTER_Y - SUN_RADIUS,
            CENTER_X + SUN_RADIUS, CENTER_Y + SUN_RADIUS,
            fill="yellow"
        )
        
        self.orbits = []
        for planet in PLANETS:
            orbit = self.canvas.create_oval(
                CENTER_X - planet["distance"], CENTER_Y - planet["distance"],
                CENTER_X + planet["distance"], CENTER_Y + planet["distance"],
                outline="white"
            )
            self.orbits.append(orbit)
        
        self.planet_objects = []
        for planet in PLANETS:
            planet_obj = self.canvas.create_oval(0, 0, 0, 0, fill=planet["color"])
            self.planet_objects.append((planet, planet_obj, 0))  # (planet data, obj, angle)
        
        self.animate()
    
    def animate(self):
        for i, (planet, obj, angle) in enumerate(self.planet_objects):
            angle += planet["speed"]
            x = CENTER_X + planet["distance"] * math.cos(angle)
            y = CENTER_Y + planet["distance"] * math.sin(angle)
            r = planet["radius"]
            self.canvas.coords(obj, x - r, y - r, x + r, y + r)
            self.planet_objects[i] = (planet, obj, angle)  # Update angle
        
        self.root.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    solar_system = SolarSystem(root)
    root.mainloop()
