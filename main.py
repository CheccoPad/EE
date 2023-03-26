import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

n_points = 10
dimensions = 1000
array = np.random.uniform(0, 10, (n_points, dimensions))

# x1 = np.random.uniform(0, 10, n_points)
# y1 = np.random.uniform(0, 10, n_points)
# z1 = np.random.uniform(0, 10, n_points)

x = array[:, 0]
y = array[:, 1]
z = array[:, 2]
complete = [x, y, z]

distance = sc.spatial.distance.pdist(array, metric='euclidean')

# plt.scatter(array[:, 0], array[:, 1])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x, y, z)

avg_dist = np.mean(distance)

print(f'The array: {array}')
# print(f'X: {x}')
# print(f'The array[0]: {array[0]}')
# print(f'Shape of the array: {array.shape}')
print(f'Average distance: {round(avg_dist, 1)}')

plt.show()
