import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Mandelbrot value for a given complex number 'c'
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Function to generate the Mandelbrot set image
def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    # Generate arrays of x and y values
    x_values = np.linspace(x_min, x_max, width)
    y_values = np.linspace(y_min, y_max, height)
    
    # Initialize an image array
    img = np.zeros((width, height))
    
    # Iterate over each pixel and compute the Mandelbrot value
    for i in range(width):
        for j in range(height):
            # Convert pixel coordinates to a complex number 'c'
            c = x_values[i] + 1j * y_values[j]
            
            # Compute the Mandelbrot value for 'c'
            img[i, j] = mandelbrot(c, max_iter)
    
    return img

# Set parameters for generating the Mandelbrot set image
width, height = 800, 800
x_min, x_max = -2.5, 1.5
y_min, y_max = -2.0, 2.0
max_iter = 100

# Generate the Mandelbrot set image
mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)

# Display the Mandelbrot set image using a color map
plt.figure(figsize=(10, 10))
plt.imshow(np.log(mandelbrot_image), cmap='inferno', extent=(x_min, x_max, y_min, y_max))
plt.colorbar(label='Log Iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
