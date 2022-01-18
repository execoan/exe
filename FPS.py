# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:48:17 2022

@author: yunus
"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import timeit

def fps(points, n_samples):
    """
    points: [N, 3] array containing the whole point cloud
    n_samples: samples you want in the sampled point cloud typically << N 
    """
    points = np.array(points)
    points_train = []
    points_test = []
    # Represent the points by their indices in points
    points_left = np.arange(len(points)) # [P]

    # Initialise an array for the sampled indices
    sample_inds = np.zeros(n_samples, dtype='int') # [S]

    # Initialise distances to inf
    dists = np.ones_like(points_left) * float('inf') # [P]

    # Select a point from points by its index, save it
    selected = 0
    sample_inds[0] = points_left[selected]

    # Delete selected 
    points_left = np.delete(points_left, selected) # [P - 1]

    # Iteratively select points for a maximum of n_samples
    for i in range(1, n_samples):
        # Find the distance to the last added point in selected
        # and all the others
        last_added = sample_inds[i-1]
        
        dist_to_last_added_point = (
            (points[last_added] - points[points_left])**2).sum(-1) # [P - i]

        # If closer, updated distances
        dists[points_left] = np.minimum(dist_to_last_added_point, 
                                        dists[points_left]) # [P - i]

        # We want to pick the one that has the largest nearest neighbour
        # distance to the sampled points
        selected = np.argmax(dists[points_left])
        sample_inds[i] = points_left[selected]

        # Update points_left
        points_left = np.delete(points_left, selected)

    for i in range(len(points)):
        if i in sample_inds:
            points_train.append(points[i])
        else:
            points_test.append(points[i])
    
    return np.array(points_train), np.array(points_test)


### 3D[imension] ###
#np.random.seed(1)
points_data = np.random.random((1000,3))
fig = plt.figure()
ax = fig.gca(projection='3d')
points_train, points_test = fps(points_data,100)
ax.scatter(points_train.T[0],points_train.T[1],points_train.T[2],c='blue')
ax.scatter(points_test.T[0],points_test.T[1],points_test.T[2],c='orange')

plt.show()

"""
points_data = np.random.random((10000,25))
new_points = fps(points_data,1000)
"""












