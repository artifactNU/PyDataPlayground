import numpy as np
import matplotlib.pyplot as plt

# --- Diffusion Simulation using NumPy and Matplotlib ---
# Use Case: Simulating the diffusion of particles in a confined space.
# Theory: The simulation illustrates how particles spread out over time due to their random motion.

# Parameters
diffusion_coefficient = 0.01  # Diffusion coefficient
initial_concentration = 1.0   # Initial concentration at the center
grid_size = 100               # Number of grid points in each dimension
time_steps = 100              # Number of time steps
delta_x = 0.1                 # Grid spacing
delta_t = 0.01                # Time step

# Initialize concentration grid
concentration = np.zeros((grid_size, grid_size))
concentration[grid_size // 2, grid_size // 2] = initial_concentration

# Perform diffusion simulation
for _ in range(time_steps):
    next_concentration = np.copy(concentration)
    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            next_concentration[i, j] = concentration[i, j] + (diffusion_coefficient * delta_t / delta_x**2) * (
                concentration[i + 1, j] + concentration[i - 1, j] + concentration[i, j + 1] + concentration[i, j - 1] - 4 * concentration[i, j]
            )
    concentration = next_concentration

# Plot the diffusion process
plt.figure(figsize=(8, 6))
plt.imshow(concentration, cmap='viridis', origin='lower', extent=(0, grid_size, 0, grid_size))
plt.colorbar(label='Concentration')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diffusion Simulation')
plt.show()
