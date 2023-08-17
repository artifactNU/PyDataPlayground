import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the equations of motion for planetary motion
def planetary_motion(t, state, G, M):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    dxdt = vx
    dydt = vy
    dvxdt = -G * M * x / r**3
    dvydt = -G * M * y / r**3
    return [dxdt, dydt, dvxdt, dvydt]

# Parameters
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 1.989e30  # Mass of the Sun in kg

# Initial conditions: position and velocity
initial_state = [1.496e11, 0, 0, 2.978e4]  # Initial position: 1 AU, Initial velocity: Earth's orbital velocity

# Time points
t_span = (0, 3.154e7)  # One year in seconds
t_eval = np.linspace(*t_span, num=1000)

# Solve the differential equations
solution = solve_ivp(planetary_motion, t_span, initial_state, t_eval=t_eval, args=(G, M))

# Extract position
x = solution.y[0]
y = solution.y[1]

# Plot the planetary orbit
plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.scatter(0, 0, color='yellow', marker='o', label='Sun')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Planetary Motion')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='datalim')
plt.show()
