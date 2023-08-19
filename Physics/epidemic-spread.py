import numpy as np
import matplotlib.pyplot as plt

# --- Epidemic Spread Simulation using NumPy and Matplotlib ---
# Use Case: Simulating the spread of an epidemic in a population.
# Theory: The simulation models the transmission of a contagious disease within a population.

# Parameters
population_size = 1000    # Total population size
initial_infected = 5      # Initial number of infected individuals
transmission_rate = 0.2   # Probability of transmission between an infected and susceptible individual
recovery_rate = 0.1       # Probability of recovery and immunity

# Time points
num_days = 100
time_points = np.arange(num_days)

# Initialize arrays to track the number of individuals in different states
susceptible = np.zeros(num_days)
infected = np.zeros(num_days)
recovered = np.zeros(num_days)

# Initialize initial infected individuals
infected[0] = initial_infected
susceptible[0] = population_size - initial_infected

# Simulate epidemic spread
for day in range(1, num_days):
    new_infections = np.random.binomial(susceptible[day - 1], transmission_rate * infected[day - 1] / population_size)
    new_recoveries = np.random.binomial(infected[day - 1], recovery_rate)
    
    susceptible[day] = susceptible[day - 1] - new_infections
    infected[day] = infected[day - 1] + new_infections - new_recoveries
    recovered[day] = recovered[day - 1] + new_recoveries

# Plot the epidemic spread
plt.figure(figsize=(10, 6))
plt.plot(time_points, susceptible, label='Susceptible')
plt.plot(time_points, infected, label='Infected')
plt.plot(time_points, recovered, label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Epidemic Spread Simulation')
plt.legend()
plt.grid(True)
plt.show()
