# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:53:10 2022

@author: ATelford
"""
import numpy as np

#function

def calculate_least_wastage(basket_item_values, discounts, order_of_discounts=None):
    
    item_values_matrix = np.array([basket_item_values for i in discounts])
    total_discount_matrix = item_values_matrix.copy()
    
    for d in enumerate(discounts):
        if d[1][1] == 'percent':
            total_discount_matrix[d[0]] *= (1 - d[1][0])
        else:
            total_discount_matrix[d[0]] -= d[1][0]
            
    total_discount_matrix[total_discount_matrix < 0] = 0
    
    total_discount_matrix -= item_values_matrix
    
    difference_matrix = np.apply_along_axis(lambda x: x - x[0], 1, total_discount_matrix)
    
    #find biggest and second biggest difference by row
    biggest_index = difference_matrix.argsort(axis=1)[:, 0]
    second_biggest_index = difference_matrix.argsort(axis=1)[:, 1]
    
    wastage_potential = [difference_matrix[i, biggest_index[i]] - difference_matrix[i, second_biggest_index[i]] for i in range(len(discounts))]
    
    best_use_index = np.argmin(wastage_potential)
    
    if order_of_discounts is None:
        expended_discount = discounts.pop(best_use_index)
        order_of_discounts = [f'{expended_discount[1]} discount of {expended_discount[0]} applied to value of {basket_item_values[biggest_index[best_use_index]]} at position {best_use_index}']
    else:
        expended_discount = discounts.pop(best_use_index)
        order_of_discounts += [f'{expended_discount[1]} discount of {expended_discount[0]} applied to value of {basket_item_values[biggest_index[best_use_index]]} at position {best_use_index}']
    
    basket_item_values[biggest_index[best_use_index]] += total_discount_matrix[best_use_index, biggest_index[best_use_index]]
    
    if len(discounts) == 0:
        return(basket_item_values, ' -> '.join(order_of_discounts))
    else:
        return(calculate_least_wastage(basket_item_values, discounts, order_of_discounts))   
    
#examples
basket_item_values_ = [50.0, 25.0]
discounts_ = [(50, 'fixed'), (0.5, 'percent')]

calculate_least_wastage(basket_item_values_, discounts_)

basket_item_values_ = [24.0, 20.0]
discounts_ = [(22, 'fixed'), (0.9, 'percent')]

calculate_least_wastage(basket_item_values_, discounts_)
    

basket_item_values_ = [10.0, 20.0, 30.0]
discounts_ = [(14, 'fixed'), (22, 'fixed'),  (0.7, 'percent')]

calculate_least_wastage(basket_item_values_, discounts_)


basket_item_values_ = [4.0, 20.0, 30.0]
discounts_ = [(14, 'fixed'), (2, 'fixed'),  (0.3, 'percent')]

calculate_least_wastage(basket_item_values_, discounts_)

basket_item_values_ = [30.0, 20.0, 4.0]
discounts_ = [(14, 'fixed'), (2, 'fixed'),  (0.3, 'percent')]

calculate_least_wastage(basket_item_values_, discounts_)
    
basket_item_values_ = [90.0, 20.0, 4.0]
discounts_ = [(99, 'fixed'), (32, 'fixed'),  (0.9, 'percent')]

calculate_least_wastage(basket_item_values_, discounts_)
    
    
            
       
            
    
    
    
    
    
    