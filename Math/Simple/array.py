import numpy as np

# --- Create and Manipulate Arrays using NumPy ---

# Create a simple array
data = np.array([1, 2, 3, 4, 5])

# Perform some basic operations on the array
mean = np.mean(data)          # Calculate the mean of the array elements
total_sum = np.sum(data)      # Calculate the sum of the array elements
square_root = np.sqrt(data)   # Calculate the square root of each element in the array

# Display the results
print("Original data:", data)
print("Mean:", mean)
print("Sum:", total_sum)
print("Square root:", square_root)
