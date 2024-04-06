#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:12:41 2024

@author: abdiel

Here we implement a coin toss simulator. As a binary distribution process and by the law of large numbers, as the number of
simulations increases, the distribution of heads (and therefore tails) approaches 50 %
"""
import numpy as np
import matplotlib.pyplot as plt
import random

def Simulate():
    tries_vec = []
    head_ratio_vec = []  
    scale_of_simulations = 1000 # parameter that controls the number of simulations
    for j in range(scale_of_simulations):      
      result = Toss_coin(j)
      tries, head_ratio = Calculate_head_ratio(result)
      
      tries_vec.append(tries)
      head_ratio_vec.append(head_ratio)
    return tries_vec, head_ratio_vec   

def Toss_coin(size_sim):
    simulations = int(1e1*size_sim) # delta increase in the number of simulations
    coin_result = np.zeros(simulations)
    for i in range(simulations):
        coin = random.randint(0, 1)
        coin_result[i] = coin
            
    return coin_result        
            
def Calculate_head_ratio(result):
    iteration = []
 
    for i,r in enumerate(result):
        iteration.append(i)
    
    #head  = 1
    total_head = result.sum()  
    try:
        tries = iteration[-1]
    except:
        tries = 1
        
    head_ratio = total_head/tries
    return tries, head_ratio
  
   # plt.plot(iteration,result)   
    
def plot_results(tries_vec,head_ratio_vec): 
    plt.xlabel("Coin tosses")
    plt.ylabel("ratio of heads over tails")
    plt.title("Coin toss simulation")
    plt.plot(tries_vec,head_ratio_vec)   
     
    
if __name__ == "__main__":
    tries_vec, head_ratio_vec = Simulate()
    plot_results(tries_vec,head_ratio_vec)

