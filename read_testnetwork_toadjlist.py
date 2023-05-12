# -*- coding: utf-8 -*-
"""
Created on Wed Jan 4 11:06:51 2023

@author: Sarah
"""

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
    G.add_edge(a, b) 
adj_list = {}
for u, v in edges:
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    adj_list[v].append(u)
    
#print(edges)
    
#print ("done reading the file")
"""
def edges_to_adj_list(edges):
    adj_list = {}
    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list
"""
#print(adj_list)