import numpy as np
import matplotlib.pyplot as plt

# --- Brownian Motion Simulation with Particle Collisions using NumPy and Matplotlib ---
# Use Case: Simulating the motion of particles undergoing Brownian motion with occasional collisions.
# Theory: The simulation models the random motion of particles and their interactions when they collide.

# Parameters
num_particles = 10              # Number of particles
num_steps = 1000                # Number of time steps
step_size = 0.1                 # Step size
collision_probability = 0.1     # Probability of a collision at each step

# Generate random initial positions for particles
initial_positions = np.random.rand(num_particles, 2) * 10

# Simulate Brownian motion with collisions
trajectories = np.zeros((num_particles, num_steps + 1, 2))
trajectories[:, 0, :] = initial_positions

for i in range(num_steps):
    random_steps = np.random.randn(num_particles, 2) * np.sqrt(step_size)
    trajectories[:, i + 1, :] = trajectories[:, i, :] + random_steps
    
    for j in range(num_particles):
        if np.random.rand() < collision_probability:
            trajectories[j, i + 1, :] = np.random.rand(2) * 10

# Plot trajectories
plt.figure(figsize=(10, 6))
for i in range(num_particles):
    plt.plot(trajectories[i, :, 0], trajectories[i, :, 1], label=f'Particle {i + 1}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Brownian Motion with Particle Collisions')
plt.legend()
plt.grid(True)
plt.show()
