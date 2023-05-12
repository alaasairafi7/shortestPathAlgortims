# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 05:37:49 2023

@author: alaa
"""
#adjecinty list

import time
import networkx as nx

def get_line():
     with open('network.txt') as file:
         for i in file:
             yield i

def readgraph():
    myset = set()
    G = nx.Graph()
    lines_required = 500
    #edges = []
    gen = get_line()
    chunk = [i for i, j in zip(gen, range(lines_required))]
    for i in chunk:
        tmp = i.split()
        #edges.append((int(tmp[0]),int(tmp[1].replace('\n',''))))
        a = tmp[0]
        b = tmp[1].replace('\n','').replace('q','')
        G.add_edge(a,b)
    return G

Graph = readgraph()
visited = [] # List for visited nodes.
queue = []   #Initialize a queue

def bfs(visited, graph, node): #function for BFS10
  visited.append(node)
  queue.append(node)
  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print(m, end = " ")
    for neighbour in graph.adj[str(m)]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
start = input("Enter Start: ")
print("Following is the Breadth-First Search")
t = time.perf_counter()
bfs(visited, Graph,start)
print("\ntime=",time.perf_counter()-t)


