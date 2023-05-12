# -*- coding: utf-8 -*-
"""
Created on Fri Jan  26 17:18:47 2023

@author: Sarah
"""
from heapq import heappush, heappop

def heuristic(node, goal):
    """calculate heuristic value, you can use any other heuristic function you prefer"""
    return abs(node - goal)

def a_star(graph, start, goal):
    """
    graph: adjacency dictionary of dictionaries
    start: starting node
    goal: target node
    """
    heap = [(0, start)]  # initialize heap with 0 distance from start to start
    came_from = {start: None}  # keeps track of the path
    cost_so_far = {start: 0}  # keeps track of the cost to reach each node
    while heap:
        current = heappop(heap)[1]  # get the node with the lowest distance from start,  (priority, node) [1] is used instead of [0] is because we want to assign the node to the variable current, not the priority(cost). 
        if current == goal:
            break  # we have reached the goal
        for neighbor in graph[current]:  # for each neighbor of the current node
            new_cost = cost_so_far[current] + graph[current][neighbor]  # the cost to reach this neighbor is the sum of the cost to reach the current node and the cost to move from current to neighbor
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:#checks if the neighbor has not been seen before or if the new cost to reach the neighbor is less than the previously recorded cost to reach the same neighbor
                cost_so_far[neighbor] = new_cost # if we visit it for first time or we have less cost than the one it has
                priority = new_cost + heuristic(neighbor, goal)  # f(n) = g(n) + h(n)
                heappush(heap, (priority, neighbor))#(priority, node)
                came_from[neighbor] = current # for the given neighbor node, the previous node in the path from the start to the current node is stored in the "came_from" dictionary.
    return came_from  # returns the path from start to goal

