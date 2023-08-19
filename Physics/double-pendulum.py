import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Double Pendulum Simulation using NumPy, Matplotlib, and SciPy ---
# Use Case: Simulating the motion of a double pendulum.
# Theory: The simulation illustrates the chaotic and complex motion of a double pendulum.

# Parameters
L1 = 1.0  # Length of the first pendulum arm (meters)
L2 = 1.0  # Length of the second pendulum arm (meters)
m1 = 1.0  # Mass of the first pendulum bob (kilograms)
m2 = 1.0  # Mass of the second pendulum bob (kilograms)
g = 9.81  # Acceleration due to gravity (m/s^2)

# Define the equations of motion for the double pendulum
def double_pendulum(t, state):
    theta1, theta2, p1, p2 = state
    c = np.cos(theta1 - theta2)
    s = np.sin(theta1 - theta2)
    denominator = m1 + m2 * s**2

    dtheta1dt = p1 / (m1 * L1**2) - m2 * g * L2 / (m1 * L1**2) * np.sin(theta1) - m2 * L2 / (denominator * L1) * p2 * np.cos(theta1 - theta2)
    dtheta2dt = p2 / (m2 * L2**2) + (m1 + m2) * g * L1 / (m2 * L2**2) * np.sin(theta2) + L1 / (denominator * L2) * p1 * np.cos(theta1 - theta2)

    dp1dt = -m2 * L1 / (denominator * L1) * p1 * p2 * np.sin(theta1 - theta2) - (m1 + m2) * g * L1 / (m1 * L1**2) * np.sin(theta1)
    dp2dt = L2 / (denominator * L2) * p1 * p2 * np.sin(theta1 - theta2) - m2 * g * L2 / (m2 * L2**2) * np.sin(theta2)

    return [dtheta1dt, dtheta2dt, dp1dt, dp2dt]

# Initial conditions: angles and momenta
initial_state = [np.pi/2, np.pi/2, 0, 0]

# Time points
t_span = (0, 10)
t_eval = np.linspace(*t_span, num=1000)

# Solve the differential equations
solution = solve_ivp(double_pendulum, t_span, initial_state, t_eval=t_eval)

# Extract angles
theta1 = solution.y[0]
theta2 = solution.y[1]

# Convert polar coordinates to Cartesian coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Plot the double pendulum motion
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label='Pendulum 1')
plt.plot(x2, y2, label='Pendulum 2')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Double Pendulum Simulation')
plt.legend()
plt.grid(True)
plt.show()
