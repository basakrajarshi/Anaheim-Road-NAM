# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:16:10 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Anaheim")
file_to_read = open(datafolder / "Anaheim-flow-2.txt")

file_to_write = open(datafolder / "Anaheim-flow-3.txt", "w")

volumes = {}
costs = {}

for line in file_to_read:
    line = line.replace(":","\t")
    line = line.replace(";", "\t")
    k = line.split()
    l = k[0] + "\t" + k[1] + "\t" + k[2] + "\t" + k[3] + "\t" + "\n"
    file_to_write.write(l)
    #print(l)
    
#---------------------------------------------------------------------


        