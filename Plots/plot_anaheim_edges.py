# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:08:34 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Anaheim")
file_to_open = datafolder / "Anaheim_edge_list.txt"

graph = nx.read_edgelist(file_to_open)

# Top 20 edges with highest betweennness centrality for unweighted graph

edges = [('277', '266'), ('378', '361'), ('299', '277'), ('404', '405'),
         ('315', '299'), ('358', '333'), ('273', '272'), ('357', '358'),
         ('408', '407'), ('147', '148'), ('308', '295'), ('295', '294'),
         ('267', '268'), ('321', '305'), ('389', '390'), ('400', '401'),
         ('290', '269'), ('319', '303'), ('138', '139'), ('356', '357')]
nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_edges(graph, pos,
                       edgelist = edges, width=5, alpha=0.9, edge_color='g')

#plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_test_1", dpi = 400)
plt.axis('off')
plt.show()

# Top 20 edges with highest change in cost for weighted graph

edges = [('4'  , '233'), ('2'  , '62' ), ('388', '372'), ('179', '180'),
         ('333', '321'), ('271', '193'), ('337', '44' ), ('120', '400'),
         ('200', '199'), ('315', '299'), ('320', '321'), ('258', '69' ),
         ('316', '300'), ('80' , '259'), ('248', '374'), ('348', '18' ),
         ('320', '312'), ('389', '390'), ('321', '305'), ('389', '50' )]
nx.draw_spectral(graph, node_size = 1)
pos = nx.spectral_layout(graph)
nx.draw_networkx_edges(graph, pos,
                       edgelist = edges, width=5, alpha=0.9, edge_color='b')

plt.savefig("Transportation-Networks-Data/Anaheim/Anaheim_top_20_change_weighted_corrected", dpi = 400)
plt.axis('off')
plt.show()
