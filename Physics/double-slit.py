import numpy as np
import matplotlib.pyplot as plt

# --- Double-Slit Experiment Simulation using NumPy and Matplotlib ---
# Use Case: Simulating the double-slit experiment to demonstrate wave-particle duality.
# Theory: The simulation shows how interference patterns emerge when particles exhibit both wave-like and particle-like behavior.

# Parameters
wavelength = 0.1      # Wavelength of the particles/waves
slit_distance = 1.0   # Distance between the two slits
screen_distance = 5.0 # Distance from the slits to the screen
screen_width = 10.0   # Width of the screen
num_points = 1000     # Number of points on the screen

# Generate the screen positions
screen_positions = np.linspace(-screen_width/2, screen_width/2, num_points)

# Calculate the interference pattern
intensity_pattern = np.zeros(num_points)
for i, x in enumerate(screen_positions):
    intensity_pattern[i] = (np.cos(np.pi * slit_distance * np.sin(2 * np.pi * x / wavelength) / (wavelength * screen_distance)))**2

# Plot the interference pattern
plt.figure(figsize=(10, 6))
plt.plot(screen_positions, intensity_pattern)
plt.xlabel('Screen Position')
plt.ylabel('Intensity')
plt.title('Double-Slit Experiment Simulation')
plt.grid(True)
plt.show()
