import numpy as np
import matplotlib.pyplot as plt

# ---random data statisitcal analysis--- numpy, matplotlib

# Generate random data
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=1000)  # Generating 1000 random samples from a normal distribution

# Calculate statistics
mean = np.mean(data)
std_dev = np.std(data)
min_val = np.min(data)
max_val = np.max(data)

# Create a histogram
plt.hist(data, bins=30, density=True, alpha=0.7, color='blue')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(mean + std_dev, color='green', linestyle='dashed', linewidth=2, label='Mean + Std Dev')
plt.axvline(mean - std_dev, color='green', linestyle='dashed', linewidth=2, label='Mean - Std Dev')
plt.legend()
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)