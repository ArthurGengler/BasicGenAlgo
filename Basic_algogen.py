# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:28:41 2021

@author: Arthur Gengler
"""

import numpy as np
import random
import operator


""""#1 Initial population generated randomly"""
def generate_ind():
    individu=np.zeros(8)
    for i in range(0,8):
        individu[i]=random.randrange(0,2)
    return individu

def generate_pop():
    pop=np.zeros((8,8))
    for i in range(0,8):
        pop[i][:]=generate_ind()
    return pop

""""#2 Evaluate the objective function for each individual """
def compute_fitness(ind):
    sum =0
    for i in range(0,8):
        sum=sum+ind[i]
    return sum

def sort_pop(pop):
    return sorted(pop, key = compute_fitness, reverse = True)
    

""""#3 Selection of individual"""
def selection_best_ones(sorted_pop):
    best_pop=np.zeros((4,8))
    for i in range(0,4):
        best_pop[i][:]=sorted_pop[i]
    return best_pop

"""#4 Crossover """
def crossover(ind1,ind2):
    new_ind=np.zeros(8)
    for i in range(0,4):
        new_ind[i]=ind1[i]
    for i in range(4,8):
        new_ind[i]=ind2[i]
    return new_ind

def pop_crossover(best_pop):
    crossed_pop=np.zeros((4,8))
    crossed_pop[0][:]=best_pop[0]
    for i in range(1,4):
        crossed_pop[i][:]=crossover(best_pop[i-1],best_pop[i])
    return crossed_pop
    
"""#5 Mutation and new gen """
def mutation(ind):
    if (ind[1]==0):
        ind[1]=1
    return ind

def mutation_of_pop(crossed_pop):
    muted_pop=np.zeros((4,8))
    for i in range(0,4):
        muted_pop[i][:]=mutation(crossed_pop[i])
    return muted_pop   
  
def new_gen(muted_pop):
    new_pop=np.zeros((8,8))
    for i in range(0,4):
        new_pop[i][:]=muted_pop[i][:]
    for i in range(4,8):
        new_pop[i][:]=generate_ind()
    return new_pop
  
"""Loop until stopping criterion"""

population = generate_pop()
for i in range(0,100): 
    sorted_pop = sort_pop(population)
    selected_pop = selection_best_ones(sorted_pop) 
    crossed_pop = pop_crossover(selected_pop)
    muted_pop = mutation_of_pop(crossed_pop)
    population = new_gen(muted_pop)

    
