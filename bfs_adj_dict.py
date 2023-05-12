# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 05:37:49 2023

@author: alaa
"""

import collections
import networkx as nx
import time


def get_line():
    with open('network.txt') as file:
        for i in file:
            yield i


vertix = []
myset = set()
G = nx.Graph()
file_name = 'network.txt'
edges = []
nodes = set()
lines_required = 500
gen = get_line()
chunk = [i for i, j in zip(gen, range(lines_required))]
for i in chunk:
    tmp = i.split()
    edges.append((int(tmp[0]), int(tmp[1].replace('\n', ''))))
    a = int(tmp[0])
    b = int(tmp[1].replace('\n', '').replace('q', ''))
    vertix.append(a)
    vertix.append(b)
    G.add_edge(a, b)

print("done reading the file")


def edges_to_adj_dict(n, edges):
    adj_dict = collections.defaultdict(dict)
    for (u, v) in edges:
        adj_dict[u][v] = 1
        adj_dict[v][u] = 1
    return dict(adj_dict)


n = max(max(u, v) for u, v in edges) + 1
adj_dict = edges_to_adj_dict(n, edges)
print(adj_dict, end=" ")

visited = []
queue = []


def bfs(graph, start2, visited2):
    visited2.append(start2)
    queue.append(start2)
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for i in adj_dict[vertex].keys():
            if i not in visited2:
                visited2.append(i)
                queue.append(i)

    return visited


# Driver Code
start = int(input("\nEnter Start: "))
print("Following is the Breadth-First Search")
t = time.perf_counter()
bfs(adj_dict, start, visited)
print("\ntime=", time.perf_counter() - t)
