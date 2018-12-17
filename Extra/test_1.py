# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:15:32 2018

@author: rajar
"""

import networkx as nx
#graph = nx.read_edgelist('test_edgelist.txt', 
#                         nodetype=int, 
#                         data=(('weight',float),))

graph = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt",
                     create_using =nx.MultiGraph(),
                     nodetype = int,
                     data=[('volume',float),('cost',float)])
#print(graph.nodes())
#print(graph.edges(data = True))

edges = []
volumes = []
costs = []

a = {}

count = 0
for i in graph.edges(data = True):
    #print(i[0],i[1], i[2], i[3])
    #print(i[0], i[1], i[2])
    count += 1
    edges.append((i[0], i[1]))
    a = i[2]
    volumes.append(a['volume'])
    costs.append(a['cost'])
    #print(type(i[2]))
    
#    volumes[(i[0],i[1])] = i[2[1]]
#    costs[(i[0],i[1])] = i[3[1]]

#print(len(graph.edges()))
#print(count)
#
#nx.draw_spectral(graph, node_size = 1)
#plt.show()
graph_2 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-net-3.txt",
                     create_using =nx.MultiGraph(),
                     nodetype = int,
                     data=[('capacity',int),('length',int), 
                           ('free-flow-time', float), ('B', float),
                           ('power', int), ('speed', int),
                           ('toll', int), ('type', int)])
    


edges_2 = []
capacities = []
lengths = []
free_flow_times = []
Bs = []
powers = []
speeds = []
tolls = []
types = []

b = {}

count = 0
for j in graph_2.edges(data = True):
    count += 1
    edges_2.append((j[0], j[1]))
    b = j[2]
    capacities.append(b['capacity'])
    lengths.append(b['length'])
    free_flow_times.append(b['free-flow-time'])
    Bs.append(b['B'])
    powers.append(b['power'])
    speeds.append(b['speed'])
    tolls.append(b['toll'])
    types.append(b['type'])
    
#print(count)

all_pairs = []
for i in graph.nodes():
    for j in graph.nodes():
        if (i != j):
            #print(i,j)
            all_pairs.append((i,j))
            
shortest_paths = {}
shortest_path_lengths = {}
for j in all_pairs:
    sp = nx.dijkstra_path(graph, j[0], j[1])
    spl = nx.dijkstra_path_length(graph, j[0], j[1])
    #print(j[0], j[1])
    #print(sp)
    #print(spl)
    #print()
    shortest_paths[j] = sp
    shortest_path_lengths[j] = spl
    
shortest_paths_1 = {}
shortest_path_lengths_1 = {}

for i in graph.nodes():
    for j in graph.nodes():
        if (i != j):
            #print(i, type(i))
            #print(j, type(j))
            sp = nx.dijkstra_path(graph, i, j)
            spl = nx.dijkstra_path_length(graph, i, j)
            p = (i,j)
            shortest_paths_1[p] = sp
            shortest_path_lengths_1[p] = spl