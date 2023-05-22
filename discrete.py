import numpy as np
import scipy as sc
import random

iterations = 1000

x = 1  # define the step size
arr = np.arange(0, 10+x, x)
# s1 = random.choice(values)
# s2 = random.choice(values)


def avg_distance(values, rep):
    print(values)
    tot = 0
    for i in range(0, rep-1):
        x1, x2, y1, y2, z1, z2 = random.choices(values, k=6)
        print(f'{x1} {x2} {y1} {y2} {z1} {z2}')
        p1 = [x1, y1, z1]
        p2 = [x2, y2, z2]
        array = [p1, p2]
        dist = sc.spatial.distance.pdist(array, 'cityblock')
        tot += dist[0]
    avg = round(tot/rep, 5)
    return avg


print(avg_distance(arr, 100000))

# print(f'{s1}, {s2}')
