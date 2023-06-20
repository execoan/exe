# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:23:07 2023

@author: yunus
"""

import numpy as np 
import matplotlib.pyplot as plt
from mayavi import mlab 

def generate_random_sample_cartesian():
    x,y,z = np.random.randint(-100,100,3)/100
    normalizer = np.sqrt(x**2+y**2+z**2)
    x_norm, y_norm, z_norm = x/normalizer,y/normalizer,z/normalizer 
    return x_norm,y_norm,z_norm


points = []
for i in range(10000):
    points.append(generate_random_sample_cartesian())
points = np.array(points)

    
mlab.plot3d(points.T[0], points.T[1], points.T[2],transparent=True, representation='points', color=(0.8,0.3,0.5))
mlab.show()