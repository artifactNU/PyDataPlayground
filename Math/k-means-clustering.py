import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq

# --- K-Means Clustering using NumPy, Matplotlib, and SciPy ---

# Generate synthetic data
np.random.seed(42)
data = np.vstack((np.random.randn(100, 2) * 0.5 + [2, 2],
                  np.random.randn(100, 2) * 0.5 + [-2, -2],
                  np.random.randn(100, 2) * 0.5 + [2, -2]))

# Perform K-Means clustering
k = 3  # Number of clusters
centroids, _ = kmeans(data, k)
cluster_ids, _ = vq(data, centroids)

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=cluster_ids, cmap='viridis', label='Data Points')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=100, color='red', label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.legend()
plt.grid(True)
plt.show()
