# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 00:10:04 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import operator as op
import numpy as np
import time

graph1 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt", 
                          data = False)

deg = []
degree_count = {}
for i in graph1.nodes():
    #print(graph1.degree(i))
    if (graph1.degree(i) not in degree_count):
        degree_count[graph1.degree(i)] = 1
    else:
        degree_count[graph1.degree(i)] += 1
    deg.append(graph1.degree(i))
        
plt.hist(deg, normed=False, bins=50)
plt.ylabel('Degree Distribution')
plt.xlabel('Degree of Node')
plt.savefig('Anaheim_Degree_Distribution', dpi = 400)
plt.show()

#d = sum(deg)/len(deg)
#print(d)
    
#print(graph1.neighbors())

avg_neighbour_degree = nx.average_neighbor_degree(graph1)
avg_neigh = []
for key,val in avg_neighbour_degree.items():
    avg_neigh.append(val)
    
plt.hist(avg_neigh, normed=False, bins=50)
plt.ylabel('Neighbour Degree Distribution')
plt.xlabel('Degree of Neighbor of Node')
plt.savefig('Anaheim_Neighbor_Degree_Distribution', dpi = 400)
#plt.show()