import numpy as np
import matplotlib.pyplot as plt

# Parameters
h_bar = 1.0  # Reduced Planck constant
m = 1.0  # Particle mass
L = 10.0  # Length of the potential well
n_points = 200  # Number of grid points
V0 = 100.0  # Potential energy at the barrier
E = 50.0  # Initial guess for energy eigenvalue

# Spatial grid
x = np.linspace(0, L, num=n_points)
dx = x[1] - x[0]

# Kinetic energy operator
T = - (h_bar**2 / (2 * m)) * (np.diag(np.ones(n_points - 1), -1) - 2 * np.diag(np.ones(n_points)) + np.diag(np.ones(n_points - 1), 1)) / dx**2

# Potential energy operator
V = np.diag(np.where(x < L/2, 0, V0))

# Hamiltonian operator
H = T + V

# Solve the Schrödinger equation using eigenvalue decomposition
eigenvalues, eigenvectors = np.linalg.eigh(H)

# Normalize the eigenvectors
normalized_eigenvectors = eigenvectors / np.sqrt(dx)

# Calculate the probability distribution for the ground state
ground_state_prob = normalized_eigenvectors[:, 0]**2

# Plot the probability distribution
plt.figure(figsize=(10, 6))
plt.plot(x, ground_state_prob)
plt.xlabel('Position')
plt.ylabel('Probability')
plt.title('Particle in a Potential Well')
plt.grid(True)
plt.show()
