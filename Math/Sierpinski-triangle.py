import numpy as np
import matplotlib.pyplot as plt

# Function to compute the midpoint of two points
def midpoint(p1, p2):
    return (p1 + p2) / 2

# Function to recursively generate the Sierpinski Triangle
def sierpinski(p1, p2, p3, depth):
    if depth == 0:
        plt.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'r')
    else:
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        
        sierpinski(p1, p12, p31, depth - 1)
        sierpinski(p12, p2, p23, depth - 1)
        sierpinski(p31, p23, p3, depth - 1)

triangle_size = 300
depth = 5

p1 = np.array([0, 0])
p2 = np.array([triangle_size, 0])
p3 = np.array([triangle_size / 2, triangle_size * np.sqrt(3) / 2])

plt.figure(figsize=(6, 6))
sierpinski(p1, p2, p3, depth)
plt.title('Sierpinski Triangle')
plt.axis('equal')
plt.axis('off')
plt.show()
