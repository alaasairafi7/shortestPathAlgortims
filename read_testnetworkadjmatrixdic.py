# -*- coding: utf-8 -*-
"""
Created on Tue Jan  24 05:37:49 2023

@author: Sarah
"""

import collections
import networkx as nx


def get_line():
     with open('C:/Users/96650/Downloads/UDITwitterCrawlAug2012Network/testnetwork.txt') as file:
         for i in file:
             yield i


vertix = []
myset = set()
G = nx.Graph()
file_name= 'testnetwork.txt'
edges = []
nodes= set()
lines_required = 100
gen = get_line()
chunk = [i for i, j in zip(gen, range(lines_required))]
for i in chunk:
    tmp = i.split()
    edges.append((int(tmp[0]),int(tmp[1].replace('\n',''))))
    a = int(tmp[0])
    b = int(tmp[1].replace('\n','').replace('q',''))
    vertix.append(a)
    vertix.append(b)
    G.add_edge(a, b) 
 
#print(edges)  
#print(len(edges))  
  
#print ("done reading the file")

def edges_to_adj_dict(n, edges):
    adj_dict = collections.defaultdict(dict)
    for (u, v) in edges:
        adj_dict[u][v] = 1
        adj_dict[v][u] = 1
    return dict(adj_dict)

n = max(max(u, v) for u, v in edges) + 1
adj_dict = edges_to_adj_dict(n, edges)
#print(adj_dict)