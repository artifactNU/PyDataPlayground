import numpy as np

# ---array--- numpy

# Create a simple array
data = np.array([1, 2, 3, 4, 5])

# Perform some basic operations
mean = np.mean(data)
total_sum = np.sum(data)
square_root = np.sqrt(data)  # Calculate the square root of each element

print("Original data:", data)
print("Mean:", mean)
print("Sum:", total_sum)
print("Square root:", square_root)
