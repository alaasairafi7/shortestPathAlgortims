# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:05:30 2023

@author: Sarah
"""
import time
import Astar_AdjList as Astarlist
import Astar_adjmatrixdic as Astardictionary
import read_testnetworkadjmatrixdic as read_adjdc
import read_testnetwork_toadjlist as read_adjlist


selection = ''
while selection != '3':
    print("1-A star algorithm(adjacency list)\n2-A star algorithm(adjacency dictionary of dictionaries)\n3-Exit")
    selection =input("Please Select:")
    if selection == '1':  #A star algorithm(adjacency list) 
        start_time = time.perf_counter()#for caculate the time
        start1 =int(input("Please enter the start:"))#take start node from the user
        goal1 =int(input("Please enter your goal:"))#take goal node from the user
        path1=Astarlist.a_star(read_adjlist.adj_list, start1, goal1)
        end_time = time.perf_counter()#for caculate the time
        print(path1)
        print("time=",end_time-start_time)

    elif selection == '2':  #A star algorithm(adjacency dictionary of dictionaries)  
        startt_time = time.perf_counter()#for caculate the time
        start2 =int(input("Please enter the start:"))#take start node from the user
        goal2 =int(input("Please enter your goal:"))#take goal node from the user
        path2=Astardictionary.a_star(read_adjdc.adj_dict, start2, goal2)
        endd_time = time.perf_counter()#for caculate the time
        print(path2)
        print("time=",endd_time-startt_time)




