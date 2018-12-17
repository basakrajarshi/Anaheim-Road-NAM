# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:07:34 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import operator as op
import numpy as np
import time

#start_time = time.time()

# This contains the edges with the volumes and the costs
graph2 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt",
                     create_using = nx.MultiGraph(),
                     nodetype = int,
                     data = [('volume',float),('cost',float)])

# Compute the betweenness centrality for weighted graph
bc_flow_w = nx.edge_current_flow_betweenness_centrality(graph2,
                                                         normalized=True,
                                                         weight='cost',
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
cost_w_2 = 0
for k in all_pairs_2:
    spl = nx.dijkstra_path_length(graph2, k[0], k[1], weight = 'cost')
    cost_w_2 += spl
    
cost_w_bef = cost_w_2/len(all_pairs_2)

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
    #print('The edge is :', edge)
    # Remove the edge under inspection from graph
    #print(len(graph1.edges()))
    graph2.remove_edge(edge_w[0], edge_w[1])
    #print(len(graph1.edges()))
    # For all pairs of nodes in the graph:
    cost_w_2 = 0
    cost_w_aft = 0
    delta_c_w = 0
    for k in all_pairs_2:
        # Compute and store the dijkstra shortest paths
        spl = nx.dijkstra_path_length(graph2, k[0], k[1], weight = 'cost')
        # Find sum of all the shortest paths
        cost_w_2 += spl
    # Divide by the number of node pairs in graph to normalize
    cost_w_aft = cost_w_2/len(all_pairs_2)
    #print('Cost after' , cost_uw_aft)
    # Find change delta_c from sum of all paths before edge removal
    delta_c_w = cost_w_aft - cost_w_bef
    #print('Change :' , delta_c)
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
    
    elapsed_time = time.time() - start_time
    print((elapsed_time)/60, 'minutes')
    
# Plotting the figure 
plt.scatter(xw, yw, alpha=0.5, color = 'b')
plt.xlabel('Betweenness Centrality of removed edge')
plt.ylabel('Change in shortest path length')
#plt.title('Change in net shortest paths vs. Edge betweenness')
plt.savefig('Change_vs_Betweenness_Anaheim_Weighted-First-60-nodes', dpi = 300)
plt.show()
#
#elapsed_time = time.time() - start_time
#
#print((elapsed_time/3600), 'hours')         