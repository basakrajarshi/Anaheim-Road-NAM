# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:48:31 2018

@author: rajar
"""

import networkx as nx
import operator as op

graph1 = nx.read_edgelist("test_edgelist_2.txt", data=False)

graph2 = nx.read_edgelist("test_edgelist.txt",
                          create_using = nx.MultiGraph(),
                          nodetype = int,
                          data=[('weight',float)])

all_pairs_1 = []
for i in graph1.nodes():
    for j in graph1.nodes():
        if (i != j):
            #print(i,j)
            all_pairs_1.append((i,j))
            
all_pairs_2 = []
for i in graph2.nodes():
    for j in graph2.nodes():
        if (i != j):
            #print(i,j)
            all_pairs_2.append((i,j))
            
edge_mini_uw = nx.edge_betweenness_centrality(graph1, 
                                              normalized = True, 
                                              weight = None)

sorted_bets_mini_uw = sorted(edge_mini_uw.items(), 
                             key = op.itemgetter(1), 
                             reverse = True)

edge_mini_w = nx.edge_betweenness_centrality(graph2, 
                                             normalized = True,
                                             weight = 'weight')

sorted_bets_mini_w = sorted(edge_mini_w.items(),
                            key = op.itemgetter(1),
                            reverse = True)

#for i in graph1.edges():
#    print(i)
#    
#for i in graph2.edges():
#    print(i)

#for i in graph1.nodes():
#    for j in graph2.nodes():
#        if (i != j):
#            a = nx.get_edge_data(i,j)
#            print(a)


edge_flow_mini = nx.edge_current_flow_betweenness_centrality(graph2,
                                                             normalized = True,
                                                             weight='weight',
                                                             solver='full')

flow_mini = sorted(edge_flow_mini.items(),
                            key = op.itemgetter(1),
                            reverse = True)

edge_flow_mini_2 = nx.edge_current_flow_betweenness_centrality(graph2,
                                                             normalized = True,
                                                             weight=None,
                                                             solver='full')

flow_mini_2 = sorted(edge_flow_mini_2.items(),
                            key = op.itemgetter(1),
                            reverse = True)














