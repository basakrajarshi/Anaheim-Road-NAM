# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:52:42 2018

@author: rajar
"""

import networkx as nx

graph2 = nx.read_edgelist("test_edgelist_2.txt", data=False)

all_pairs_2 = []
for i in graph2.nodes():
    for j in graph2.nodes():
        if (i != j):
            #print(i,j)
            all_pairs_2.append((i,j))
            
shortest_paths_2 = {}
shortest_path_lengths_2 = {}
for j in all_pairs_2:
    sp = nx.dijkstra_path(graph, j[0], j[1])
    spl = nx.dijkstra_path_length(graph, j[0], j[1])
    #print(j[0], j[1])
    #print(sp)
    #print(spl)
    #print()
    shortest_paths_2[j] = sp
    shortest_path_lengths_2[j] = spl