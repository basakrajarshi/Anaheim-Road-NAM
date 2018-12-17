# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:45:56 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import operator as op
import numpy as np
import time

graph1 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt", 
                          data = False)

# This contains the edges with the volumes and the costs
graph2 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt",
                     create_using = nx.MultiGraph(),
                     nodetype = int,
                     data = [('volume',float),('cost',float)])

# Degree
deg_assort = nx.degree_assortativity_coefficient(graph1)
avg_neighbour_degree = nx.average_neighbor_degree(graph1)
avg_neigh = []
for key,val in avg_neighbour_degree.items():
    avg_neigh.append(val)



# Triangles
triangles = nx.triangles(graph1)
triangle_count = 0
for key,val in triangles.items():
    if (val == 1):
        triangle_count += 1
        
# Transitivity
trans = nx.transitivity(graph1)

#Clustering
clusters = nx.clustering(graph1)
cluster_count = 0
for key,val in clusters.items():
    if (val != 0):
        cluster_count += 1
        
# Average Clustering
avg_clsuters = nx.average_clustering(graph1)

# Squares
squares = nx.square_clustering(graph1)
square_count = 0
for key,val in squares.items():
    if (val != 0):
        square_count += 1
        
# Diameter
dia = nx.diameter(graph1)
rad = nx.radius(graph1)
        
print('Number of triangles :', triangle_count)
print('Transitivity :',trans)
print('Number of clusters :', cluster_count)
print('Average clusters :', avg_clsuters)
print('Number of squares :', square_count)
print('Diameter', dia)
print('Radius', rad)
print('Average Neighbor degree :', 
      sum(avg_neigh)/len(avg_neigh))
print('Degree Assortativity :', deg_assort)