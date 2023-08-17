import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_particles = 10  # Number of particles
num_steps = 100  # Number of time steps
step_size = 0.1  # Step size

# Generate random initial positions for particles
initial_positions = np.random.rand(num_particles, 2) * 10

# Simulate Brownian motion
trajectories = np.zeros((num_particles, num_steps + 1, 2))
trajectories[:, 0, :] = initial_positions

for i in range(num_steps):
    random_steps = np.random.randn(num_particles, 2) * np.sqrt(step_size)
    trajectories[:, i + 1, :] = trajectories[:, i, :] + random_steps

# Plot trajectories
plt.figure(figsize=(10, 6))
for i in range(num_particles):
    plt.plot(trajectories[i, :, 0], trajectories[i, :, 1], label=f'Particle {i + 1}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Brownian Motion Simulation')
plt.legend()
plt.grid(True)
plt.show()
