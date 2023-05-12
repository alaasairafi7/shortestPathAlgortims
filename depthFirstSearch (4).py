#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 07:59:24 2023

@author: ritalshafiei
"""
from collections import defaultdict
import time
import networkx as nx


# list

def get_line():
     with open('testnetwork.txt') as file:
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
def adjListDFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    #visited.add(start)
    visited.append(start)
    print(start, end=" ")
    for node in graph[start]:
        if node not in visited:
            adjListDFS(graph, node, visited)
            
# matrix 
class AdjMat:
    """
    Class to create an adjacency matrix
    Takes as input the name of the textfile
    """

    def __init__(self, textfile):
        self.V = 0
        self.graph= defaultdict(dict)
        self.fill_graph(textfile)
        for i in range(self.V):
            for j in range(self.V):
                if j not in self.graph[i]:
                    self.graph[i][j] = 0

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
        self.V = max(self.V-1, u, v) + 1

    def fill_graph(self, textfile):
         with open(textfile, "r") as f:
            for edge in f:
                edge_values = edge.split("\t")
                if len(edge_values) < 2:
                    continue
                x, y = edge_values
                self.add_edge(int(x), int(y))
            return None
   

    def DFSUtil(self, vertex, visited):
        visited[vertex] = True
        print(vertex,end=" ")
        for i in range(self.V):
            if self.graph[vertex][i] == 1 and not visited[i]:
                self.DFSUtil(i, visited)


    def DFS(self, v):
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
        print()

     
def main():
    while True:
        print("Menu:")
        print("1. dfs on Adjacency List ")
        print("2. dfs on Adjacency Matrix ")
        print("0. Exit")
        option = int(input("Select From Menu:"))

        if option == 1:
            
            source = input("Enter the source: ")
            print("DFS: ")
            t = time.perf_counter()
            adjListDFS(Graph,source,visited)
            print("\ntime=",time.perf_counter()-t)
            
        elif option == 2: 
            file = "testnetwork.txt"
            graph = AdjMat(file)
            source = input("Enter the source: ")
            t = time.perf_counter()
            vertex = int(input())
            graph.DFS(vertex)
            
            
            print("\ntime=",time.perf_counter()-t)
        else:
            break
        
if __name__ == "__main__":
    main()

    





































 