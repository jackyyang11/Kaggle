# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:13:59 2018

@author: Jacky
"""

# =============================================================================
# # Set up decay learning rate
# =============================================================================
def learning_rate_power(current_round):
    base_learning_rate = 0.19000424246380565
    min_learning_rate = 0.01
    lr = base_learning_rate * np.power(0.995,current_round)
    return max(lr, min_learning_rate)