# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:33:05 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import operator as op
import numpy as np
import time

#start_time = time.time()

# This contains the edges with the volumes and the costs
graph1 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt", 
                          data = False)

# Compute the betweenness centrality for weighted graph
bc_flow_w = nx.edge_current_flow_betweenness_centrality(graph1,
                                                         normalized=True,
                                                         weight=None,
                                                         solver='full')

sorted_bc_flow_w = sorted(bc_flow_w.items(), 
                           key = op.itemgetter(1), 
                           reverse=True)

all_pairs_2 = []
for i in graph2.nodes():
    for j in graph2.nodes():
        if (i != j):
            all_pairs_2.append((i,j))
            
# Compute and store the sum of all dijkstra shortest paths
# divided by the number of node pairs
shortest_paths_w = {}
shortest_path_lengths_w = {}
cost_w_2 = 0
for k in all_pairs_2:
    sp = nx.dijkstra_path(graph2, k[0], k[1], weight = 'cost')
    spl = nx.dijkstra_path_length(graph2, k[0], k[1], weight = 'cost')
    cost_w_2 += spl
    shortest_paths_w[k] = sp
    shortest_path_lengths_w[k] = spl
    
cost_w_bef = cost_w_2/len(all_pairs_2)

#------------------------------------------------------------------

# Compute the change in cost as a function of centraity of
# removed edge
edge_number_w = 0
change_in_path_w = {}

xw = []
yw = []
# Go through each edge in the graph
for edge_data_w in sorted_bc_flow_w:
    
    start_time = time.time()
    
    edge_w = edge_data_w [0]
    #print('The edge is :', edge_w)
    
    # Remove the edge under inspection from graph
    #print(len(graph2.edges()))
    graph2.remove_edge(edge_w[0], edge_w[1])
    #print(len(graph2.edges()))
    
    cost_w_2 = 0
    cost_w_aft = 0
    delta_c_w = 0
    # For all pair of nodes in the graph:
    for k in all_pairs_2:
        # Fetch the shortest path from the shortest_path_w dictionary
        path = shortest_paths_w[k]
        #print(path, len(path))
        # Check if edge is there in the shortest path
        m = any([edge_w[0], edge_w[1]] == path[i:i+2] for i in range(len(path) - 1))
        # If the removed edge is there in the 
        # current shortest path
        if (m == True):
            #print(m)
            # Find sum of all the shortest paths
            cost_w_2 += len(path)
            #print(len(path))
        # Else
        else: 
            #print(m)
            # Recalculate the shortest path and store the length
            spl = nx.dijkstra_path_length(graph2, k[0], k[1], weight = 'cost')
            # Find sum of all the shortest paths
            cost_w_2 += spl
    # Divide by the number of node pairs in graph to normalize
    cost_w_aft = cost_w_2/len(all_pairs_2)
    #print('Cost after' , cost_uw_aft)
    # Find change delta_c from sum of all paths before edge removal
    delta_c_w = cost_w_aft - cost_w_bef
    #print('Change :' , delta_c_w)
    # Fetch edge centrality from bc_flow_uw dictionary
    ec = bc_flow_w[edge_w]
    #print('Edge centrality :' , ec)
    # Store centrality (key) and delta_c (value) in a dictionary
    change_in_path_w[(edge_w, ec)] = delta_c_w
    
    xw.append(ec)
    yw.append(delta_c_w)
    
    # Add edge (without weight) back to the graph 
    graph2.add_edge(edge_w[0], edge_w[1])
    #print(len(graph1.edges()))
    
    # Count edges completed
    edge_number_w += 1
    print('Edge number :', edge_number_w)
    #print()
    

    
# Plotting the figure 
plt.scatter(xw, yw, alpha=0.5, color = 'b')
plt.xlabel('Betweenness Centrality of removed edge')
plt.ylabel('Change in shortest path length')
#plt.title('Change in net shortest paths vs. Edge betweenness')
plt.savefig('Change_vs_Betweenness_Anaheim_Weighted', dpi = 300)
plt.show()  

elapsed_time = time.time() - start_time
print((elapsed_time)/3600, 'hours') 


sorted_change_in_path_w = sorted(change_in_path_w.items(), 
                           key = op.itemgetter(1), 
                           reverse=True)