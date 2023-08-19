import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- Predator/Prey Model using Lotka-Volterra Equations ---
# Dependencies: numpy, matplotlib, scipy

# Lotka-Volterra equations
def lotka_volterra(X, t, alpha, beta, gamma, delta):
    """
    Lotka-Volterra equations describing predator-prey dynamics.

    Parameters:
    X (array): Array containing prey and predator populations.
    t (array): Time points for integration.
    alpha (float): Prey birth rate.
    beta (float): Predation rate.
    gamma (float): Predator death rate.
    delta (float): Reproduction rate of predators.

    Returns:
    array: Rates of change for prey and predator populations.
    """
    prey, predator = X
    dprey_dt = alpha * prey - beta * prey * predator
    dpredator_dt = delta * prey * predator - gamma * predator
    return np.array([dprey_dt, dpredator_dt])

# Parameters
alpha = 0.1
beta = 0.02
gamma = 0.3
delta = 0.01

# Initial conditions
initial_conditions = np.array([40, 9])

# Time points
t = np.linspace(0, 500, 1000)

# Solve the differential equations
solution = odeint(lotka_volterra, initial_conditions, t, args=(alpha, beta, gamma, delta))

# Extract prey and predator populations from the solution
prey_population = solution[:, 0]
predator_population = solution[:, 1]

# Plot the populations over time
plt.figure(figsize=(10, 6))
plt.plot(t, prey_population, label='Prey')
plt.plot(t, predator_population, label='Predator')
plt.title('Predator-Prey Dynamics (Lotka-Volterra Model)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()
