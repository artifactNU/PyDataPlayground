import numpy as np
import matplotlib.pyplot as plt

# ---linear regression--- numpy, matplotlib

# Generate some synthetic data with noise
np.random.seed(42)
x_data = np.linspace(0, 10, 50)
y_data = 2.5 * x_data + 1.5 + 2.5 * np.random.normal(size=50)

# Fit the curve to the data
params, covariance = np.polyfit(x_data, y_data, deg=1, cov=True)

# Extract the fitted parameters
slope, intercept = params

# Generate the fitted curve
fitted_y = slope * x_data + intercept

# Plot the original data and the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data with Noise')
plt.plot(x_data, fitted_y, label='Fitted Curve: y={:.2f}x + {:.2f}'.format(slope, intercept), color='orange')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()