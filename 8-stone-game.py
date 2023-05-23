# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:30:36 2023

@author: yunus
"""

import numpy as np
import matplotlib.pyplot as plt
from numba import njit

def plot_array(array,title):
    fig = plt.figure(dpi = 200)
    n_array = array.copy().T
    f = n_array.T[0].copy()
    l = n_array.T[2].copy()
    n_array.T[2] = f
    n_array.T[0] = l

    for i, y in enumerate(n_array):
        for j, x in enumerate(y): 
            plt.text(i, j, str(x), color="red", fontsize=260)
            plt.text(i+0.03, j+0.028, str(x), color="blue", fontsize=235)
    plt.axis('off')
    plt.title(title,loc=('center'))
    plt.show()

@njit
def error(a, b):
    return np.sum(np.abs(a - b))

def control(mat):
    pass

#
def moves(matrice, goal):
    
    n_error = []
    pos = np.where(matrice == 0)
    i, j = pos[0][0], pos[1][0]
    mats = []
    i_err = error(matrice, goal)
     
    if  j > 0:
            n_mat = matrice.copy() 
            n_mat[i][j-1], n_mat[i][j] = matrice[i][j], matrice[i][j-1]
            mats.append(n_mat)
            n_error.append(error(goal, n_mat))
    if  j < 2:
            n_mat = matrice.copy() 
            n_mat[i][j+1], n_mat[i][j] = matrice[i][j], matrice[i][j+1]
            mats.append(n_mat)
            n_error.append(error(goal, n_mat))
    if  i > 0:
            n_mat = matrice.copy() 
            n_mat[i-1][j], n_mat[i][j] = matrice[i][j], matrice[i-1][j]
            mats.append(n_mat)
            n_error.append(error(goal, n_mat))
    if  i < 2:
            n_mat = matrice.copy() 
            n_mat[i+1][j], n_mat[i][j] = matrice[i][j], matrice[i+1][j]
            mats.append(n_mat)
            n_error.append(error(goal, n_mat))
              
    if np.random.rand()>0.4:
        rand = np.random.randint(0,len(mats))
        mats = mats[rand]
    else:    
        if min(n_error) < i_err:
            mats = mats[np.argmin(n_error)]   
        else:
            rand = np.random.randint(0,len(mats))
            mats = mats[rand]
    return  mats

truth = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)

#initial = np.array([1,2,3,4,5,6,7,8,0])
#np.random.shuffle(initial)
#initial = initial.reshape((3,3))

initial = np.array([[4, 5, 6], [1, 2, 3], [7, 8, 0]])

err = error(truth, initial)


mat = initial.copy()
k=0


while err>1 and k<1000:
    k+=1
    mat = moves(mat, truth)   
    err = error(mat, truth)
    if k%100==0:
        plot_array(mat,f'              Step: {k} Err: {err}')
    #mat, n_error = moves(initial,truth)

    
