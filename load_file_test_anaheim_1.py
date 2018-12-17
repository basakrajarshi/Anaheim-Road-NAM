# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:26:14 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Anaheim")
file_to_open = datafolder / "Anaheim_edge_list.txt"

#file = open(filetoopen)
#next(file)


#for line in file:
#    print(line)

#file_to_write = open("Anaheim_edge_list.txt", "w")
#
#nodes = {}
#count = 1
#for line_a in file:
#    k = line_a.strip().split('\t')
#    #print
#    file_to_write.write(k[0] + '\t' + k[1] + '\n')
#    
#file_to_write.close()
#file.close()

graph = nx.read_edgelist(file_to_open)

#nx.draw_circular(graph, node_size = 1)
#plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_draw_circular", dpi = 400)
#plt.show()
#
#nx.draw_kamada_kawai(graph, node_size = 1)
#plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_draw_kamada_kawai", dpi = 400)
#plt.show()
#
#nx.draw_random(graph, node_size = 1)
#plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_draw_random", dpi = 400)
#plt.show()

nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_edges(graph, pos,
                       edgelist=[('6','213'), ('7','214'),('7', '253'),('9','379')], width=5, alpha=0.5, edge_color='r')

plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_test_1", dpi = 400)
plt.axis('off')
plt.show()

#nx.draw_spring(graph, node_size = 1)
#plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_draw_spring", dpi = 400)
#plt.show()
#
#nx.draw_shell(graph, node_size = 1)
#plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_draw_shell", dpi = 400)
#plt.show()
#
#print(len(graph.nodes()))
#print(len(graph.edges()))

