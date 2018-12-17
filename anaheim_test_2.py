# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:59:37 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import operator as op
import numpy as np
import time

start_time = time.time()

# Read and store the graph for the weighted data 
# Anaheim-flow-3.txt


graph1 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt", 
                          data = False)

# This contains the edges with the volumes and the costs
graph2 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt",
                     create_using = nx.MultiGraph(),
                     nodetype = int,
                     data = [('volume',float),('cost',float)])

#print(len(graph2.nodes()))
#print(len(graph2.edges()))

# Compute the betweenness centrality for unweighted graph
bc_flow_uw = nx.edge_current_flow_betweenness_centrality(graph1,
                                                         normalized=True,
                                                         weight=None,
                                                         solver='full')

bc_flow_uw_correct = {}

for (key, value) in bc_flow_uw.items():
    newkey_1 = int(key[0])
    newkey_2 = int(key[1])
    newkey = (newkey_1, newkey_2)
    bc_flow_uw_correct[newkey] = value

sorted_bc_flow_uw = sorted(bc_flow_uw_correct.items(), 
                           key = op.itemgetter(1), 
                           reverse=True)

# Compute the betweenness centrality for weighted graph
bc_flow_w = nx.edge_current_flow_betweenness_centrality(graph2,
                                                         normalized=True,
                                                         weight='cost',
                                                         solver='full')

sorted_bc_flow_w = sorted(bc_flow_w.items(), 
                           key = op.itemgetter(1), 
                           reverse=True)

#for e in graph1.edges():
#    print(e)

#graph1.remove_edge('396', '410')

all_pairs_1 = []
for i in graph1.nodes():
    for j in graph1.nodes():
        if (i != j):
            all_pairs_1.append((i,j))

# Compute and store the sum of all dijkstra shortest paths
# divided by the number of node pairs
cost_uw_1 = 0
for k in all_pairs_1:
    spl = nx.dijkstra_path_length(graph1, k[0], k[1])
    cost_uw_1 += spl
    
cost_uw_bef = cost_uw_1/len(all_pairs_1)


# Compute the change in cost as a function of centraity of
# removed edge
edge_number = 0
change_in_path = {}

x = []
y = []
# Go through each edge in the graph
for edge_data in sorted_bc_flow_uw:
    edge = edge_data [0]
    #print('The edge is :', edge)
    # Remove the edge under inspection from graph
    #print(len(graph1.edges()))
    graph1.remove_edge(str(edge[0]), str(edge[1]))
    #print(len(graph1.edges()))
    # For all pairs of nodes in the graph:
    cost_uw_2 = 0
    cost_uw_aft = 0
    delta_c = 0
    for k in all_pairs_1:
        # Compute and store the dijkstra shortest paths
        spl = nx.dijkstra_path_length(graph1, k[0], k[1])
        # Find sum of all the shortest paths
        cost_uw_2 += spl
    # Divide by the number of node pairs in graph to normalize
    cost_uw_aft = cost_uw_2/len(all_pairs_1)
    #print('Cost after' , cost_uw_aft)
    # Find change delta_c from sum of all paths before edge removal
    delta_c = cost_uw_aft - cost_uw_bef
    #print('Change :' , delta_c)
    # Fetch edge centrality from bc_flow_uw dictionary
    ec = bc_flow_uw_correct[edge]
    #print('Edge centrality :' , ec)
    # Store centrality (key) and delta_c (value) in a dictionary
    change_in_path[(edge, ec)] = delta_c
    
    x.append(ec)
    y.append(delta_c)
    
    # Add edge (without weight) back to the graph 
    graph1.add_edge(str(edge[0]), str(edge[1]))
    #print(len(graph1.edges()))
    
    # Count edges completed
    edge_number += 1
    print('Edge number :', edge_number)
    #print()
    
# Plotting the figure 
plt.scatter(x, y, alpha=0.5, color = 'b')
plt.xlabel('Betweenness Centrality of removed edge')
plt.ylabel('Change in shortest path length')
plt.title('Change in net shortest paths vs. Edge betweenness')
plt.savefig('Change_vs_Betweenness_Anaheim_Unweighted', dpi = 300)
plt.show()

elapsed_time = time.time() - start_time

print((elapsed_time/3600), 'hours')
    