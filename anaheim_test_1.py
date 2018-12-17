# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:02:33 2018

@author: rajar
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time

start_time = time.time()

# Read and store the graph for only the edges (unweighted)
# Anaheim-flow-3.txt
# Set data = False

graph1 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt", 
                          data = False)

# Store all the pairs of nodes

all_pairs_1 = []
for i in graph1.nodes():
    for j in graph1.nodes():
        if (i != j):
            all_pairs_1.append((i,j))
            
# Compute and store all the shortest geodesic paths and path lengths

shortest_paths_1 = {}
shortest_path_lengths_1 = {}
for k in all_pairs_1:
    sp = nx.dijkstra_path(graph1, k[0], k[1])
    spl = nx.dijkstra_path_length(graph1, k[0], k[1])
    
    new = []
    for s in sp:
        new.append(int(s))
        
    c = int(spl)
    
    jj = (int(k[0]), int(k[1]))
    
    shortest_paths_1[jj] = new
    shortest_path_lengths_1[jj] = c
    
# Read and store the graph for the weighted data 
# Anaheim-flow-3.txt
# This contains the edges with the volumes and the costs

graph2 = nx.read_edgelist("Transportation-Networks-Data/Anaheim/Anaheim-flow-3.txt",
                     create_using = nx.MultiGraph(),
                     nodetype = int,
                     data = [('volume',float),('cost',float)])

# Store all the pairs of nodes

all_pairs_2 = []
for i in graph2.nodes():
    for j in graph2.nodes():
        if (i != j):
            all_pairs_2.append((i,j))
            
# Compute and store all the shortest paths and 
# shortest path lengths according to cost

shortest_paths_2 = {}
shortest_path_lengths_2 = {}
for l in all_pairs_2:
    sp = nx.dijkstra_path(graph2, l[0], l[1], weight = 'cost')
    spl = nx.dijkstra_path_length(graph2, l[0], l[1], weight = 'cost')
    shortest_paths_2[l] = sp
    shortest_path_lengths_2[l] = spl
    
geo_length_values = []

for v in shortest_path_lengths_1.values():
    geo_length_values.append(v)
    
cost_length_values = []

for w in shortest_paths_2.values():
    cost_length_values.append(len(w))
    
#print(max(cost_length_values))
    
# Histograms for geodesic shortest paths

# Histrogram for geodesic shortest path lengths with 50 bins
plt.hist(geo_length_values, normed=True, bins=50)
plt.xlabel('Shortest Geodesic Path Lengths')
plt.ylabel('Density')
plt.title('Histogram for shortest path lengths in Anaheim network')
plt.savefig('Anaheim-shortest-geodesic-path-length_hist-50-bins', 
            dpi = 300)
plt.show()

# Histrogram for geodesic shortest path lengths with 25 bins
plt.hist(geo_length_values, normed=True, bins=25)
plt.xlabel('Shortest Geodesic Path Lengths')
plt.ylabel('Density')
plt.title('Histogram for shortest path lengths in Anaheim network')
plt.savefig('Anaheim-shortest-geodesic-path-length_hist-25-bins', 
            dpi = 300)
plt.show()

# Constructing the fraction table for 5 sized
# Make 5 lists 
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
# Iterate through each vertex pair
for (k1, v1), (k2, v2) in zip(shortest_paths_1.items(), shortest_paths_2.items()):
    # If the geo path length == cost path length:
    if (v1 == v2):
        # If the geodesic dist between the vertices is 1-5:
        if (len(v1) >= 2 and len(v1) <= 6):
            list_1.append(k1)
        
        # If the geodesic dist between the vertices is 6-10:
        if (len(v1) >= 7 and len(v1) <= 11):
            list_2.append(k1)
            
        # If the geodesic dist between the vertices is 11-15:
        if (len(v1) >= 12 and len(v1) <= 16):
            list_3.append(k1)
        
        # If the geodesic dist between the vertices is 16-20:
        if (len(v1) >= 17 and len(v1) <= 21):
            list_4.append(k1)
            
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) >= 22 and len(v1) <= 26):
            list_5.append(k1)
            
fraction_equal = (len(list_1)/len(all_pairs_1),
                  len(list_2)/len(all_pairs_1),
                  len(list_3)/len(all_pairs_1),
                  len(list_4)/len(all_pairs_1),
                  len(list_5)/len(all_pairs_1))

# Constructing the bar chart for 5 bins
n_groups = 5
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.55

opacity = 0.4

rects1 = ax.bar(index, fraction_equal, bar_width,
                alpha=opacity, color='b')

ax.set_xlabel('Unweighted geodesic path lengths')
ax.set_ylabel('Fraction (geodesic = minimum cost)')
ax.set_title('Equality distribution for geodesic and min cost path lengths')
ax.set_xticks(index)
ax.set_xticklabels(('1-5', '6-10', '10-15', '15-20', '20-25'))
ax.legend()

fig.tight_layout()
plt.savefig('Anaheim-Fraction-plot_geodesic=minimumcost_5-bins', 
            dpi = 300)
plt.show()

# -----------------------------------------------------------------

# Constructing the fraction table for 1 sized
# Make 25 lists 
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []
list20 = []
list21 = []
list22 = []
list23 = []
list24 = []
list25 = []

# Iterate through each vertex pair
for (k1, v1), (k2, v2) in zip(shortest_paths_1.items(), shortest_paths_2.items()):
    # If the geo path length == cost path length:
    if (v1 == v2):
        # If the geodesic dist between the vertices is 1-5:
        if (len(v1) == 2):
            list1.append(k1)
        
        # If the geodesic dist between the vertices is 6-10:
        if (len(v1) == 3):
            list2.append(k1)
            
        # If the geodesic dist between the vertices is 11-15:
        if (len(v1) == 4):
            list3.append(k1)
        
        # If the geodesic dist between the vertices is 16-20:
        if (len(v1) == 5):
            list4.append(k1)
            
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) == 6):
            list5.append(k1)
        
        # If the geodesic dist between the vertices is 20-25:    
        if (len(v1) == 7):
            list6.append(k1)
        
        # If the geodesic dist between the vertices is 6-10:
        if (len(v1) == 8):
            list7.append(k1)
            
        # If the geodesic dist between the vertices is 11-15:
        if (len(v1) == 9):
            list8.append(k1)
        
        # If the geodesic dist between the vertices is 16-20:
        if (len(v1) == 10):
            list9.append(k1)
            
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) == 11):
            list10.append(k1)
            
        if (len(v1) == 12):
            list11.append(k1)
        
        # If the geodesic dist between the vertices is 6-10:
        if (len(v1) == 13):
            list12.append(k1)
            
        # If the geodesic dist between the vertices is 11-15:
        if (len(v1) == 14):
            list13.append(k1)
        
        # If the geodesic dist between the vertices is 16-20:
        if (len(v1) == 15):
            list14.append(k1)
            
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) == 16):
            list15.append(k1)
        
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) == 17):
            list16.append(k1)
        
        # If the geodesic dist between the vertices is 6-10:
        if (len(v1) == 18):
            list17.append(k1)
            
        # If the geodesic dist between the vertices is 11-15:
        if (len(v1) == 19):
            list18.append(k1)
        
        # If the geodesic dist between the vertices is 16-20:
        if (len(v1) == 20):
            list19.append(k1)
            
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) == 21):
            list20.append(k1)
            
        if (len(v1) == 22):
            list21.append(k1)
        
        # If the geodesic dist between the vertices is 6-10:
        if (len(v1) == 23):
            list22.append(k1)
            
        # If the geodesic dist between the vertices is 11-15:
        if (len(v1) == 24):
            list23.append(k1)
        
        # If the geodesic dist between the vertices is 16-20:
        if (len(v1) == 25):
            list24.append(k1)
            
        # If the geodesic dist between the vertices is 20-25:
        if (len(v1) == 26):
            list25.append(k1)
            
fraction_equal_2 = (len(list1)/len(all_pairs_1),
                    len(list2)/len(all_pairs_1),
                    len(list3)/len(all_pairs_1),
                    len(list4)/len(all_pairs_1),
                    len(list5)/len(all_pairs_1),
                    len(list6)/len(all_pairs_1),
                    len(list7)/len(all_pairs_1),
                    len(list8)/len(all_pairs_1),
                    len(list9)/len(all_pairs_1),
                    len(list10)/len(all_pairs_1),
                    len(list11)/len(all_pairs_1),
                    len(list12)/len(all_pairs_1),
                    len(list13)/len(all_pairs_1),
                    len(list14)/len(all_pairs_1),
                    len(list15)/len(all_pairs_1),
                    len(list16)/len(all_pairs_1),
                    len(list17)/len(all_pairs_1),
                    len(list18)/len(all_pairs_1),
                    len(list19)/len(all_pairs_1),
                    len(list20)/len(all_pairs_1),
                    len(list21)/len(all_pairs_1),
                    len(list22)/len(all_pairs_1),
                    len(list23)/len(all_pairs_1),
                    len(list24)/len(all_pairs_1),
                    len(list25)/len(all_pairs_1))

# Constructing the bar chart for 5 bins
n_groups_2 = 25
fig, ax = plt.subplots()
index_2 = np.arange(n_groups_2)
bar_width_2 = 0.55

opacity = 0.4

rects1 = ax.bar(index_2, fraction_equal_2, bar_width_2,
                alpha=opacity, color='r')

ax.set_xlabel('Unweighted geodesic path lengths')
ax.set_ylabel('Fraction (geodesic = minimum cost)')
ax.set_title('Equality distribution for geodesic and min cost path lengths')
ax.set_xticks(index_2)
ax.set_xticklabels(('1', '2', '3', '4', '5' ,
                    '6', '7', '8', '9', '10',
                    '11','12','13','14','15',
                    '16','17','18','19','20',
                    '21','22','23','24','25'))
ax.legend()

fig.tight_layout()
plt.savefig('Anaheim-Fraction-plot_geodesic=minimumcost_25-bins', 
            dpi = 300)
plt.show()

elapsed_time = time.time() - start_time

print((elapsed_time/60), 'minutes')

