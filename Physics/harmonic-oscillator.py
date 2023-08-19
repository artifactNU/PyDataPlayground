import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Simple Harmonic Motion Simulation using NumPy, Matplotlib, and SciPy ---
# Use Case: Simulating the motion of a simple harmonic oscillator, like a mass attached to a spring.
# History: The study of simple harmonic motion dates back to ancient Greece and is fundamental to understanding vibrations and oscillations in various systems.

# Define the equations of motion for a simple harmonic oscillator
def simple_harmonic(t, state, omega):
    """
    Equations of motion for a simple harmonic oscillator.

    Parameters:
    t (float): Time.
    state (array): Array containing position and velocity.
    omega (float): Angular frequency.

    Returns:
    array: Rates of change for position and velocity.
    """
    x, v = state
    dxdt = v
    dvdt = -omega**2 * x
    return [dxdt, dvdt]

# Parameters
omega = 2.0  # Angular frequency

# Initial conditions: position and velocity
initial_state = [1.0, 0.0]

# Time points
t_span = (0, 10)
t_eval = np.linspace(*t_span, num=1000)

# Solve the differential equations
solution = solve_ivp(simple_harmonic, t_span, initial_state, t_eval=t_eval, args=(omega,))

# Extract position and velocity
position = solution.y[0]
velocity = solution.y[1]

# Plot the position over time
plt.figure(figsize=(10, 6))
plt.plot(solution.t, position, label='Position')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Simple Harmonic Motion')
plt.legend()
plt.grid(True)
plt.show()
