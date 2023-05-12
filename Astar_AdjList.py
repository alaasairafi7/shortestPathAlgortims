# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 02:29:29 2023

@author: Sarah

because our data structure is graph i used heap to implement this algorithm 
Heap data structure is used in A* algorithm to efficiently find the node with the lowest cost (f(n) = g(n) + h(n)),
 where g(n) is the cost so far to reach the node and h(n) is the heuristic estimate of the cost to reach the goal from the node. 
 The heap data structure allows for quick retrieval of the node with the minimum f(n) value,
 which is essential for the efficiency of the A* algorithm. 
 Other data structures such as arrays or linked lists do not provide the same level of efficiency for finding the node 
 with the minimum f(n) value, making heap a suitable choice for implementing A* algorithm. 
 -----------------------------------------------------------------------------------------
 -----------------------------------------------------------------------------------------
 The equation "return abs(node - goal)" calculates the heuristic value,
 which is an estimate of the cost from the current node to the goal node. 
 This equation is used to determine the priority of each node in the heap queue.
 ----
 which is the absolute difference between the current node and the goal node.
 This value is then added to the cost so far (g(n)) to determine the priority of each node.
 -----------------------------------------------------------------------------------------
 -----------------------------------------------------------------------------------------
 heappop is a function from the heapq module in Python. 
 It retrieves and removes the smallest element from the heap data structure. 
 In the given code, it retrieves and removes the node from the heap list with the lowest cost (distance from start node) 
 as determined by the heuristic function. This node will then be used as the current node in the next iteration of the while loop.
 -----------------------------------------------------------------------------------------
 -----------------------------------------------------------------------------------------
 
"""
    
from heapq import heappush, heappop

def heuristic(node, goal):
    """calculate heuristic value, you can use any other heuristic function you prefer"""
    return abs(node - goal)

def a_star(graph, start, goal):
    """
    graph: adjacency list of the graph
    start: starting node
    goal: target node
    """
    heap = [(0, start)]  # initialize heap with 0 distance from start to start
    came_from = {start: None}  # keeps track of the path
    cost_so_far = {start: 0}  # keeps track of the cost to reach each node
    while heap:
        current = heappop(heap)[1]  # get the node with the lowest distance from start
        if current == goal:
            break  # we have reached the goal
        for neighbor in graph[current]:  # for each neighbor of the current node
            new_cost = cost_so_far[current]  # the cost to reach this neighbor is the same as the cost to reach the current node,because it represents the total cost of moving from the start node to the neighbor
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost #current
                priority = new_cost + heuristic(neighbor, goal)  # f(n) = g(n) + h(n)
                heappush(heap, (priority, neighbor))
                came_from[neighbor] = current
    return came_from  # returns the path from start to goal

"""
#Test graph
graph = {0: [1, 2], 1: [3, 4], 2: [5, 6], 3: [], 4: [], 5: [], 6: []}
start = 0
goal = 6

path = a_star(graph, start, goal)
print(path)
"""
#############################
"""
output of test graph will be:
{0: None, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2}
This means that to get from the start node (0) to the goal node (6), 
you need to go through node 2, which is connected to node 0, 
and then node 6, which is connected to node 2.
"""
