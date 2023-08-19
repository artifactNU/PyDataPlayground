import numpy as np
import matplotlib.pyplot as plt

# --- Wave Propagation Simulation using NumPy and Matplotlib ---
# Use Case: Simulating the propagation of waves in a two-dimensional medium.
# Theory: The simulation demonstrates how waves spread and interfere, creating patterns of constructive and destructive interference.

# Parameters
wave_speed = 1.0                        # Wave propagation speed in the medium
frequency = 2.0                         # Frequency of the wave
wavelength = wave_speed / frequency     # Wavelength of the wave
amplitude = 1.0                         # Amplitude of the wave
time = 0.0                              # Initial time

# Spatial grid
grid_size = 100                         # Number of grid points in each dimension
x = np.linspace(0, 10, grid_size)
y = np.linspace(0, 10, grid_size)
X, Y = np.meshgrid(x, y)

# Calculate wave function
wave_function = amplitude * np.sin(2 * np.pi * frequency * time - 2 * np.pi * (np.sqrt(X**2 + Y**2) / wavelength))

# Plot the wave propagation
plt.figure(figsize=(8, 6))
plt.imshow(wave_function, cmap='coolwarm', extent=(0, 10, 0, 10), origin='lower', aspect='auto')
plt.colorbar(label='Amplitude')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Wave Propagation')
plt.show()
