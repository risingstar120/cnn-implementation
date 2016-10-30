# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 23:14:44 2016

@author: lenovo
"""
import numpy as np

def cmc_curve(camera1, camera2, model, rank_max=50):
    num = len(camera1)    
    similarity_order = np.zeros((num))
    rank = []
    score = []    
    for i, person1 in enumerate(camera1):
        for j, person2 in enumerate(camera2):
            s = model.predict([person1.reshape(1,160,60,3), person2.reshape(1,160,60,3)])
            similarity_rate = s[0][0]
            similarity_order[j] = similarity_rate
        similarity_rate_sorted = np.argsort(similarity_order)
        for k in range(num):
            if similarity_rate_sorted[k] == i:
                rank.append(k+1)
                break
    rank_val = 0
    for i in range(rank_max):
        rank_val = rank_val + len([j for j in rank if i == j-1])        
        score.append(rank_val / float(num))
    return np.array(score)