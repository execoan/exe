# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 01:30:55 2021

@author: yunus
"""


a = [[1,2],[3,4],[5,6],[8,9],[1,2],[1,2],[3,4],[5,6],[11,12],[0,1],[13,15],[0,1]]

def find_same(list_1):
    same_indices = []
    temp = []
    for i in range(len(a)):
        equal_list = []

        for j in range(i+1,len(a)):
            
            print(temp)
            if a[i] == a[j]:
                temp.append(j)
                equal_list.append(j)
        if i not in temp:           
           same_indices.append([i]+equal_list)
    return same_indices


print(find_same(a))
