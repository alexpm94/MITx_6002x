# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:09:14 2020

@author: japena
"""

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
items = ['coca','pepsi','fanta']

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    #If there are 2 bags, the each items has 3 states
    #bag1, bag2 or none, that's why 3^N combinations
    N = len(items)
    for i in range(3**N):
        bag1 = []
        bag2 = []
        
        for j in range(N):
            bag = (i//(3**j))%3
            if bag == 1:
                bag1.append(items[j])
            elif bag == 2:
                bag2.append(items[j])
        yield(bag1, bag2)
                
                