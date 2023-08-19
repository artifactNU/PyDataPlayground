import numpy as np
import matplotlib.pyplot as plt

# --- Numerical Integration using Trapezoidal Rule ---
# Use Case: Estimating the integral of a mathematical function using the trapezoidal rule.
# Theory: The trapezoidal rule approximates the area under a curve by dividing it into trapezoids and summing their areas.

# Define the mathematical function to integrate
def func(x):
    return x**2

# Integration parameters
a = 0       # Lower limit of integration
b = 5       # Upper limit of integration
num_intervals = 50  # Number of intervals for trapezoidal rule

# Generate x values and evaluate the function
x_values = np.linspace(a, b, num_intervals + 1)
y_values = func(x_values)

# Calculate the area under the curve using the trapezoidal rule
integral_estimate = np.trapz(y_values, x_values)

# Plot the function and the trapezoids
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Function: $x^2$')
plt.fill_between(x_values, y_values, color='lightblue', alpha=0.3, label='Trapezoids')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Numerical Integration using Trapezoidal Rule')
plt.legend()
plt.grid(True)
plt.show()

# Print the estimated integral
print("Estimated Integral:", integral_estimate)
