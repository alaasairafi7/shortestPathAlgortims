# shortestPathAlgortims
Design a data structures for big data network, implemented uisng different algorthmis BFS , DFS , A* , best first search , bidirectional search 

## project notes

Project idea:
Design data structures: present 2 data structures for a very large social network to show the shortest path In this project, you will implement and analyze the
following
BFS, DFS, Best FS, A* Search, and bidirectional bfs Assume your data structure (i.e. adjacency list) represents the input graphs. Implement the data structures and compare them in terms of time complexity.
Project Data:
Network.txt
https://drive.google.com/file/d/1WF3Fs2y8ssZEfLkvI7JasRaOOnOPLV4C/view?usp=shar e_link
test.txt
https://drive.google.com/file/d/1cda_rvjyO3vsybkAckd4rP-1ReqzwAmu/view?usp=share_link
testnetwork.txt
https://drive.google.com/file/d/1N8posPPkVNUd44eMnVyZGqyV0fzNXPNA/view?usp=share_li nk
IDE to start project:
Pycharm:
https://www.jetbrains.com/pycharm/download/#section=windows
Spayder:
https://github.com/spyder- ide/spyder/releases/latest/download/Spyder_64bit_full.exe
         
   Libraries :
- Time
- networkx as nx
- heapq
- matplotlib.pyplot as plt
- Mmnap
- math
- collections from defaultadit
How open folders:
- We have 7 files in folders shortest path Algorithms
Fist file ( A* Algorithm )
A star.zip
1- read_testnetwork_toadjlist.py :here we will read the network data from testnetwork file into a graph and pass the graph edges to adjacency list Data Structure.
2- read_testnetwork_toadjmatrixdic.py :here we will read the network data from testnetwork file into a graph and pass the graph edges to adjacency dictionary of dictionaries Data Structure.
3- Astar_AdjList.py :here we will implement A star algorithm that accept adjacency list Data Structure as input, we will use heappop and heappush which are functions from the heapq module in Python
first we have def heuristic(node, goal) which will calculate heuristic value,we will call it in a_star method. then we have def a_star(graph, start, goal) that will take as input (graph: adjacency list of the graph,start: starting node,goal: target node)
and this is the method that will do all the work and we will call it in the main to take our values.
4- Astar_adjmatrixdic.py :here we will implement A star algorithm that accept adjacency dictionary of dictionaries Data Structure as input, we will use heappop and heappush which are functions from the heapq module in Python
first we have def heuristic(node, goal) which will calculate heuristic value,we will call it in a_star method. then we have def a_star(graph, start, goal) that will take as input (graph: adjacency dictionary of dictionaries,start: starting node,goal: target node)
and this is the method that will do all the work and we will call it in the main to take our values.
  
   5-main.py :here all the work done, we will import time,import Astar_AdjList as Astarlist,import Astar_adjmatrixdic as Astardictionary,import read_testnetworkadjmatrixdic as read_adjdc,import read_testnetwork_toadjlist as read_adjlist.
And then we will have a menu so the user can choose if he want Astar take an adjacency list Data Structure or Astar take adjacency dictionary of dictionaries Data Structure, then he will pass his start,goal values.
as an output he will have a path from start node to goal node and the time estimated by the algorithm to have the shortest path.
Second file ( best fs algorithm )
BsetFristList.py
A code for best first search algorithm with an adjacency list implementation contain a method called get_line() will open the data file and then for each data in the file a method addedge() take the adjacent vertices with its edge cost and insert it to the adjacency list. The method best_first_search() will take a a source and target and the number of vertices as parameters, And in this method using a Priority Queue library a priority queue is created which is used to store the costs of nodes that have the lowest evaluation function value, Also a time library was used to count the process time for the code
Third file ( best fs algorithm )
BestFirstMatrix.py
A code for best first search algorithm with an adjacency matrix implementation contain a method called loadGraph() will open the data file and then each data in the file will be stored in an adjacency matrix called GRAPH. The method best_first_search() will take a source and target and the number of vertices as parameters, And in this method using a Priority Queue library a priority queue is created which is used to store the costs of nodes that have the lowest evaluation function value, Also a time library was used to count the process time for the code
Fourth file ( bfs algorithm )
Bfs-adj-list.py
First we have det get_line()
    
   This method to open the network text data , between () put the file path witch is network.txt.
Then we have def readgraph()
This method to read the network data as graph.
Then we have bfs methed
This method for bfs algorithm using adj_list data structure.
Fifth file ( bfs algorithm )
Bfs-adj-dict.py
First we have det get_line()
This method to open the network text data , between () put the file path witch is network.txt.
Then we have def edges-to-adj-dict()
This method to convert the graph data into matrix data.
Then we have bfs methed
This method for bfs algorithm using adj_dict data structure.
File 6 ( Bidirectional bfs ) BidirectionalSearch_Graph_data_structurelast.zip “ BidirectionalSearch" Open the folder -
.This folder contain two file and inside each file there are code
The first file is "BidirectionalSearch_Graph_data_structure" which is contained Graph data
structures.
In the “Graph" Algorithm there are some Classes(Node, BidirectionalSearch) and there is loop
.that read only 100 line from file
(Methods(add_edge, bfs, is_intersecting, print_path, bidirectional_search
The second file is "BidirectionalSearch_tree_data_structure" which is contained Binary data structures
   
   In the “Binary" Algorithm there are some Classes(Node, BinarySearchTree, BidirectionalSearch) .and there is loop that read only 100 line from file
Methods(insert, search)
Libraries: - matplotlib.pyplot as plt - mmap
File 7 ( dfs algorithm )
depthFirstSearch.py
How to Open the File:
- Open the file"depthFirstSearch “
In this code we used: from collections defaultdict library, time library, networkx as nx.
The code contains a menu it’ll ask you to enter 1 to read the testnetwork.txt file as an adjacency list then it will ask you to enter the source/ start node after that it will perform DFS on the list and print the result.
Or enter 2 to read the testnetwork.txt file as an adjacency matrix then it will ask you to enter the source/ start node after that it will perform DFS on the matrix and print the result.
The methods in this code are: get_line(), readgraph(), adjListDFS, add_edge, ill_graph, DFS , main.
