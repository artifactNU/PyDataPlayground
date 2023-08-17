import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# ---curve fitting--- numpy, matplotlib, scipy

# Generate some synthetic data with noise
np.random.seed(42)
x_data = np.linspace(0, 10, 50)
y_data = 2.5 * np.exp(-0.3 * x_data) + 0.5 * np.random.normal(size=50)

# Define the model function
def exponential_decay(x, a, b):
    return a * np.exp(-b * x)

# Fit the curve to the data
params, covariance = curve_fit(exponential_decay, x_data, y_data, p0=(2, 0.1))

# Extract the fitted parameters
fitted_a, fitted_b = params

# Generate the fitted curve
fitted_curve = exponential_decay(x_data, fitted_a, fitted_b)

# Plot the original data and the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data with Noise')
plt.plot(x_data, fitted_curve, label='Fitted Curve: a={:.2f}, b={:.2f}'.format(fitted_a, fitted_b), color='orange')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Exponential Decay Curve Fitting')
plt.legend()
plt.grid(True)
plt.show()