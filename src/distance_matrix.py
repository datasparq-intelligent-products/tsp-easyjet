import numpy as np

n = len(points)

dists = np.zeros([n, n])

for i in range(n):
    for j in range(n):
        dists[i, j] = length(points[i], points[j])