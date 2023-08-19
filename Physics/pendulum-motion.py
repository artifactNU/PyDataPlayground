import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Pendulum Motion Simulation using NumPy, SciPy, and Matplotlib ---
# Use Case: Simulating the motion of a simple pendulum under the influence of gravity.
# Theory: The simulation showcases the oscillatory behavior of a pendulum and its dependence on length and initial conditions.

# Define the equations of motion for a simple pendulum
def pendulum_motion(t, state, length, gravity):
    theta, omega = state
    dthetadt = omega
    domegadt = - (gravity / length) * np.sin(theta)
    return [dthetadt, domegadt]

# Parameters
length = 1.0       # Length of the pendulum in meters
gravity = 9.81    # Acceleration due to gravity in m/s^2
initial_state = [np.radians(30), 0]  # Initial angle: 30 degrees, Initial angular velocity: 0

# Time points
t_span = (0, 10)  # Time interval in seconds
t_eval = np.linspace(*t_span, num=1000)

# Solve the differential equations
solution = solve_ivp(pendulum_motion, t_span, initial_state, t_eval=t_eval, args=(length, gravity))

# Extract angle
theta = solution.y[0]

# Calculate pendulum position
x = length * np.sin(theta)
y = -length * np.cos(theta)

# Plot the pendulum motion
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.scatter(0, 0, color='red', marker='o', label='Pivot')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Pendulum Motion')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='datalim')
plt.show()
