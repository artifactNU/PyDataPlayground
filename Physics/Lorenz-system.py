import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# --- Lorenz Attractor Visualization using NumPy, SciPy, and Matplotlib ---
# Use Case: Visualizing chaotic behavior in a simplified atmospheric convection model known as the Lorenz system.
# History: Developed by Edward Lorenz in 1963, the Lorenz system is a classic example of deterministic chaos and sensitivity to initial conditions.

# Define the Lorenz system equations
def lorenz(t, state, sigma, rho, beta):
    """
    Equations of the Lorenz system.

    Parameters:
    t (float): Time.
    state (array): Array containing x, y, and z coordinates.
    sigma (float): Prandtl number.
    rho (float): Rayleigh number.
    beta (float): Geometric parameter.

    Returns:
    array: Rates of change for x, y, and z coordinates.
    """
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parameters
sigma = 10
rho = 28
beta = 8 / 3

# Initial conditions
initial_state = [0, 1, 0]

# Time points
t_span = (0, 50)
t_eval = np.linspace(*t_span, num=10000)

# Solve the differential equations
solution = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval, args=(sigma, rho, beta))

# Plot the Lorenz attractor
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution.y[0], solution.y[1], solution.y[2], color='b', lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.show()
