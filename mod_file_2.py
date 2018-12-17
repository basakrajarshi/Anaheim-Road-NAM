# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:41:15 2018

@author: rajar
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

datafolder = Path("Transportation-Networks-Data/Anaheim")
file_to_read = open(datafolder / "Anaheim-net-2.txt")

file_to_write = open(datafolder / "Anaheim-net-4.txt", "w")

count = 0
for line in file_to_read:
    line = line.replace(":","\t")
    line = line.replace(";", "\t")
    k = line.split()
    l = k[0] + "\t" + k[1] + "\t" + k[2] + "\t" + k[3] + "\t" + k[4] + "\t" + k[5] + "\t" + k[6] + "\t" + k[7] + "\t" + k[8] + "\t" + k[9] + "\n"
    print(l)
    file_to_write.write(l)
    count += 1
    print(count)
    #print(l)
    
print(count)