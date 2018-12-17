# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:08:08 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Anaheim")
file_to_open = datafolder / "Anaheim_edge_list.txt"

graph = nx.read_edgelist(file_to_open)

# Top centrality nodes in the network un-weighted
nodes = ['317', '330', '355', '333', '329', '299']

nodes_2 =  ['321', '266', '303', '305', '358', '315', '357', '356', 
            '388', '327', '343', '316', ]

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes,node_color='b',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_cent_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()


# Top degree centrality nodes un-weighted
nodes_degree = ['330', '303', '337', '299', '317', '266', '267',
                '269', '273', '302', '304', '308', '341', '329',
                '332', '333', '361', '369', '385', '373']

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes_degree,node_color='b',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_degree_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()

# Top harmonic centrality nodes un-weighted
nodes_harmonic = ['319', '321', '317', '330', '356', '320', '318', 
                '329', '333', '355', '316', '344', '357', '358',
                '343', '328', '303', '315', '305', '354']

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes_harmonic,node_color='r',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_harmonic_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()


# Top betweenness centrality nodes un-weighted
nodes_betweenness = ['358', '321', '305', '299', '333', '266', '277',
                     '315', '357', '384', '356', '319', '390', '385',
                     '386', '355', '388', '327', '317', '375']

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes_betweenness,node_color='g',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_betweenness_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()

# Top eigenvector centrality nodes un-weighted
nodes_eigenvector = ['317', '329', '328', '330', '343', '342', '355',
                     '316', '354', '371', '372', '356', '299', '370',
                     '341', '315', '327', '387', '388', '373']

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes_eigenvector,node_color='y',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_eigenvector_unweighted", 
            dpi = 400)
plt.axis('off')
plt.show()

# Top harmonic centrality nodes weighted
nodes_harmonic_2 = ['20', '62', '397', '413', '14', '23', '414', 
                    '21', '15', '8', '2', '412', '22', '5', '19',
                    '380', '257', '416', '415', '254']

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_nodes(graph,pos,nodelist = nodes_harmonic_2,node_color='c',
                       node_size=200, alpha=0.9)
plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_harmonic_weighted", 
            dpi = 400)
plt.axis('off')
plt.show()



