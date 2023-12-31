import numpy as np
import matplotlib.pyplot as plt

# --- Newton's Law of Cooling Simulation using NumPy and Matplotlib ---
# Use Case: Simulating the cooling of an object to its surrounding temperature over time.
# History: Newton's Law of Cooling, formulated by Isaac Newton in the 17th century, describes the rate of heat loss from an object due to the temperature difference with its surroundings.

# Parameters
initial_temperature = 100.0   # Initial temperature in degrees Celsius
ambient_temperature = 25.0    # Ambient temperature in degrees Celsius
cooling_constant = 0.1         # Cooling constant

# Time points
t = np.linspace(0, 20, num=100)

# Calculate temperature using Newton's law of cooling
temperature = ambient_temperature + (initial_temperature - ambient_temperature) * np.exp(-cooling_constant * t)

# Plot temperature decay
plt.figure(figsize=(10, 6))
plt.plot(t, temperature)
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title("Newton's Law of Cooling")
plt.grid(True)
plt.show()
