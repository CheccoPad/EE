import numpy as np
import scipy as sc


def avg_distance(n_points, dimensions, rep):
    tot = 0
    for j in range(0, rep-1):

        # Uses numpy library to quickly generate an array of random points
        # values 0 - 10; num of points given by 'n_points'; num of dimensions given by 'dimensions'
        array = np.random.uniform(0, 10, (n_points, dimensions))
        # Uses scipy library to calculate the euclidean distance between each point
        # Extremely quicker than coding the equation in python, which would be
        # terribly inefficient
        dist = sc.spatial.distance.pdist(array, 'cityblock')
        tot += dist[0]
    avg = round(tot/rep, 5)
    return avg


print(avg_distance(2, 2, 10000000))
