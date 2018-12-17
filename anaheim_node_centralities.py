# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:01:58 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import operator as op
import numpy as np
import time
import math

#start_time = time.time()

# This contains the edges without the volumes and costs
graph1 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt", 
                          data = False)

# This contains the edges with the volumes and the costs
graph2 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt",
                     create_using = nx.MultiGraph(),
                     nodetype = int,
                     data = [('volume',float),('cost',float)])




def deg_cent(graph):
    degree_centralities = {} # Dictionary for storing the degree centralities
    for j in graph.nodes(): # Iterate through each node in the graph
        degree_centralities[j] = len(graph.edges(j))
        # Storing the number of edges for each node
    
    sorted_degrees = sorted(degree_centralities.items(), 
                            key=op.itemgetter(1), reverse=True)
    # Sorting the degree centralities in decreasing order of importance
    return sorted_degrees

def harm_cent(graph):
    shortest_paths = {} # Dictionary for storing the shortest paths from each vertex
    harmonic_centralities = {} # Dictionary for storing the harmonic centralities 
    sum_of_geodesics = 0
    total_vertices = len(graph.nodes())
    for k in graph.nodes(): # Iterating through each node 
    
        shortest_paths = nx.single_source_shortest_path_length(graph,k)
        # Fidning the SSSP length from each node to all other nodes
        sum_of_geodesics = sum(shortest_paths.values())/(total_vertices - 1)
        # Summing over all the geodesics for each source vertex
        harmonic_centralities[k] = sum_of_geodesics
        # Storing the harmonic centrality for each node
        shortest_paths = {}
        
    
    sorted_harmonics = sorted(harmonic_centralities.items(), 
                              key=op.itemgetter(1))
    # Sorting the harmonic centralities in decreasing order of importance
    return sorted_harmonics

def eig_cent_1(G, max_iter=100, tol=1.0e-3, nstart=None,
                           weight=None):
    
#    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
#        raise nx.NetworkXException("Not defined for multigraphs.")
 
    if len(G) == 0:
        raise nx.NetworkXException("Empty graph.")
 
    if nstart is None:
 
        # choose starting vector with entries of 1/len(G)
        x = dict([(n,1.0/len(G)) for n in G])
    else:
        x = nstart
 
    # normalize starting vector
    s = 1.0/sum(x.values())
    for k in x:
        x[k] *= s
    nnodes = G.number_of_nodes()
 
    # make up to max_iter iterations
    for i in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast, 0)
 
        # do the multiplication y^T = x^T A
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
 
        # normalize vector
        try:
            s = 1.0/math.sqrt(sum(v**2 for v in x.values()))
 
        # this should never be zero?
        except ZeroDivisionError:
            s = 1.0
        for n in x:
            x[n] *= s
 
        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        if err < nnodes*tol:
            #return x
            sorted_eigenvector = sorted(x.items(), 
                                key=op.itemgetter(1), reverse=True)
            return sorted_eigenvector
        
def eig_cent_2(G, max_iter=100, tol=1.0e-3, nstart=None,
                           weight='cost'):
    
#    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
#        raise nx.NetworkXException("Not defined for multigraphs.")
 
    if len(G) == 0:
        raise nx.NetworkXException("Empty graph.")
 
    if nstart is None:
 
        # choose starting vector with entries of 1/len(G)
        x = dict([(n,1.0/len(G)) for n in G])
    else:
        x = nstart
 
    # normalize starting vector
    s = 1.0/sum(x.values())
    for k in x:
        x[k] *= s
    nnodes = G.number_of_nodes()
 
    # make up to max_iter iterations
    for i in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast, 0)
 
        # do the multiplication y^T = x^T A
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
 
        # normalize vector
        try:
            s = 1.0/math.sqrt(sum(v**2 for v in x.values()))
 
        # this should never be zero?
        except ZeroDivisionError:
            s = 1.0
        for n in x:
            x[n] *= s
 
        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        if err < nnodes*tol:
            #return x
            sorted_eigenvector = sorted(x.items(), 
                                key=op.itemgetter(1), reverse=True)
            return sorted_eigenvector


# Centralities for the un-weighted network
close_cent_1 = nx.closeness_centrality(graph1)
bet_cent_1   = nx.betweenness_centrality(graph1)

sorted_deg_cent_1 = deg_cent(graph1)

sorted_harm_cent_1 = harm_cent(graph1)

sorted_eig_cent_1 = eig_cent_1(graph1)

sorted_close_cent_1 = sorted(close_cent_1.items(), 
                             key = op.itemgetter(1), 
                             reverse=True)
sorted_bet_cent_1   = sorted(bet_cent_1.items(), 
                             key = op.itemgetter(1), 
                             reverse=True)


# Centralities for the weighted network
close_cent_2 = nx.closeness_centrality(graph2, distance= 'cost')
bet_cent_2   = nx.betweenness_centrality(graph2, weight = 'cost', 
                                         endpoints = True)

sorted_deg_cent_2 = deg_cent(graph2)

#sorted_harm_cent_2 = harm_cent(graph2)
harm_cent_2 = nx.harmonic_centrality(graph2, distance= 'cost')
sorted_harm_cent_2 = sorted(harm_cent_2.items(), 
                            key = op.itemgetter(1))

sorted_eig_cent_2 = eig_cent_2(graph2)

sorted_close_cent_2 = sorted(close_cent_2.items(), 
                             key = op.itemgetter(1), 
                             reverse=True)
sorted_bet_cent_2   = sorted(bet_cent_2.items(), 
                             key = op.itemgetter(1), 
                             reverse=True)
 