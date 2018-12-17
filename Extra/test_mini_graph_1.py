# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:24:49 2018

@author: rajar
"""

import networkx as nx

graph = nx.read_edgelist("test_edgelist.txt",
                     create_using = nx.MultiGraph(),
                     nodetype = int,
                     data=[('weight',float)])

weights = []

aa = {}

all_pairs = []
for i in graph.nodes():
    for j in graph.nodes():
        if (i != j):
            #print(i,j)
            all_pairs.append((i,j))
            
shortest_paths = {}
shortest_path_lengths = {}
for j in all_pairs:
    sp = nx.dijkstra_path(graph, j[0], j[1], weight = 'weight')
    spl = nx.dijkstra_path_length(graph, j[0], j[1], weight = 'weight')
    #print(j[0], j[1])
    #print(sp)
    #print(spl)
    #print()
    shortest_paths[j] = sp
    shortest_path_lengths[j] = spl
    
#nx.write_edgelist(graph, "test_edgelist_2.txt", data=False)
    
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
    sp = nx.dijkstra_path(graph2, j[0], j[1])
    spl = nx.dijkstra_path_length(graph2, j[0], j[1])
    #a = int(sp[0])
    #b = int(sp[1])
    new = []
    for s in sp:
        new.append(int(s))
    c = int(spl)
    jj = (int(j[0]), int(j[1]))
    #print(j[0], j[1])
    #print(sp)
    #print(spl)
    #print()
    #shortest_paths_2[jj] = sp
    #shortest_path_lengths_2[jj = spl
    
    shortest_paths_2[jj] = new
    shortest_path_lengths_2[jj] =   c