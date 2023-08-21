import numpy as np
import matplotlib.pyplot as plt

# Function to apply an affine transformation to a point
def transform(p, matrix, offset):
    return np.dot(matrix, p) + offset

# Function to generate Barnsley Fern points using an iterated function system
def barnsley_fern(n_points):
    points = np.zeros((n_points, 2))
    points[0, :] = [0, 0]
    
    A = np.array([[0, 0], [0, 0.16]])
    B = np.array([[0.85, 0.04], [-0.04, 0.85]])
    C = np.array([[0.2, -0.26], [0.23, 0.22]])
    D = np.array([[-0.15, 0.28], [0.26, 0.24]])
    
    probabilities = [0.01, 0.85, 0.07, 0.07]
    matrices = [A, B, C, D]
    offsets = [[0, 0], [0, 1.6], [0, 1.6], [0, 0.44]]
    
    for i in range(1, n_points):
        choice = np.random.choice(4, p=probabilities)
        points[i, :] = transform(points[i - 1, :], matrices[choice], offsets[choice])
    
    return points

n_points = 50000
fern_points = barnsley_fern(n_points)

plt.figure(figsize=(6, 8))
plt.scatter(fern_points[:, 0], fern_points[:, 1], s=1, color='green')
plt.title('Barnsley Fern')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
