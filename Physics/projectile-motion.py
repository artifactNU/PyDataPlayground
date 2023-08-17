import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_velocity = 20.0  # Initial velocity in m/s
angle_degrees = 45.0  # Launch angle in degrees
gravity = 9.81  # Acceleration due to gravity in m/s^2

# Convert angle to radians
angle_radians = np.radians(angle_degrees)

# Time of flight
time_of_flight = (2 * initial_velocity * np.sin(angle_radians)) / gravity

# Time points
t = np.linspace(0, time_of_flight, num=100)

# Calculate horizontal and vertical positions
x = initial_velocity * np.cos(angle_radians) * t
y = initial_velocity * np.sin(angle_radians) * t - 0.5 * gravity * t**2

# Plot the projectile trajectory
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Height (m)')
plt.title('Projectile Motion')
plt.grid(True)
plt.show()
