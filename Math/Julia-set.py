import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Julia set value for a given complex number 'c'
def julia(c, max_iter):
    z = c
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Function to generate the Julia set image
def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    x_values = np.linspace(x_min, x_max, width)
    y_values = np.linspace(y_min, y_max, height)
    img = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            z = x_values[i] + 1j * y_values[j]
            img[i, j] = julia(z, max_iter)
    
    return img

width, height = 800, 800
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
c = -0.7 + 0.27j  # Change this constant for different Julia sets
max_iter = 100

julia_image = julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(np.log(julia_image), cmap='inferno', extent=(x_min, x_max, y_min, y_max))
plt.colorbar(label='Log Iterations')
plt.title('Julia Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
