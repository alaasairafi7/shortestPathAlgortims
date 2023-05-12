import matplotlib.pyplot as plt
import networkx as nx
import mmap
import time

node_colors = []

class Node:
     
    def __init__(self, vertex):
         
        self.vertex = vertex
        self.next = None
 
class BidirectionalSearch:
     
    def __init__(self, vertices ,):
         
        self.vertices = vertices
        self.graph = [None] * self.vertices
         
        self.src_queue = list()
        self.dest_queue = list()
         
        self.src_visited = [False] * self.vertices
        self.dest_visited = [False] * self.vertices

        self.src_parent = [None] * self.vertices
        self.dest_parent = [None] * self.vertices
         

    def add_edge(self, src, dest):
         
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
         
    def bfs(self, direction = 'forward'):
         
        if direction == 'forward':
             
            current = self.src_queue.pop(0)
            connected_node = self.graph[current]
             
            while connected_node:
                vertex = connected_node.vertex
                 
                if not self.src_visited[vertex]:
                    self.src_queue.append(vertex)
                    self.src_visited[vertex] = True
                    self.src_parent[vertex] = current
            
                     
                connected_node = connected_node.next
        else:
             

            current = self.dest_queue.pop(0)
            connected_node = self.graph[current]
             
            while connected_node:
                vertex = connected_node.vertex
                 
                if not self.dest_visited[vertex]:
                    self.dest_queue.append(vertex)
                    self.dest_visited[vertex] = True
                    self.dest_parent[vertex] = current
                  
                     
                connected_node = connected_node.next
                 

    def is_intersecting(self):
         

        for i in range(self.vertices):
            if (self.src_visited[i] and
                self.dest_visited[i]):
                return i
                 
        return -1
 
    def print_path(self, intersecting_node,
                   src, dest):
                        
        path = list()
        path.append(intersecting_node)
        i = intersecting_node
         
        while i != src:
            path.append(self.src_parent[i])
            i = self.src_parent[i]
            node_index = list(G.nodes()).index(i)
            node_colors[node_index] = 'green'
            
    
             
        path = path[::-1]
        i = intersecting_node
        node_index = list(G.nodes()).index(i)
        node_colors[node_index] = 'red'
        
        
         
        while i != dest:
            path.append(self.dest_parent[i])
            i = self.dest_parent[i]
            node_index = list(G.nodes()).index(i)
            node_colors[node_index] = 'green'
            
  
             
        print("The Path :")
        path = list(map(str, path))
         
        print(' -> '.join(path))
     
    def bidirectional_search(self, src, dest):
        start_time = time.perf_counter()#for caculate the time
#code to calulate

        self.src_queue.append(src)
        self.src_visited[src] = True
        self.src_parent[src] = -1
         
        self.dest_queue.append(dest)
        self.dest_visited[dest] = True
        self.dest_parent[dest] = -1
 
        while self.src_queue and self.dest_queue:
             
            self.bfs(direction = 'forward')
             
    
            self.bfs(direction = 'backward')
             
        
            inode = self.is_intersecting()
             

            if inode != -1:
                print(f"Path exists between {src} and {dest}")
                print(f"Intersection at : {inode}")
                self.print_path(inode,src, dest)
                end_time = time.perf_counter()#for caculate the time
                
                print("time=",end_time-start_time)

                print("\n\nvisualizing the graph ... ")
                pos = nx.random_layout(G)
                nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=30 )
                nx.draw_networkx_edges(G, pos, width=0.5)
                labels = {node: node for node in G.nodes()}
                nx.draw_networkx_labels(G, pos, labels, font_size=6 ,font_weight=20)
                plt.show()

                exit(0)
        print(f"Path does not exist between {src} and {dest}")

        print("\n\nvisualizing the graph ... ")
        pos = nx.random_layout(G)
        nx.draw_networkx_nodes(G,pos, node_color=node_colors , node_size=30)
        nx.draw_networkx_edges(G, pos, width=0.5)
        labels = {node: node for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=6 ,font_weight=20)
        plt.show()
 

G = nx.Graph()

data_path = "/Users/NADIA.AKBER/Downloads/testnetwork.txt"

#this is the max number of lines that the program will read from the datafile because it is so big ,
#however you can get all the data if you want if you made "Get_all_data" = True

Get_all_data = False

number_of_lines_to_get_from_the_data_file = 100

n = 0

src = 38

dest = 16865781

data = {}

print("adding the data from file to the data set ...\n\n")

with open(data_path, "r") as file:
    mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    if(not Get_all_data):
     for line in range(number_of_lines_to_get_from_the_data_file):
        line = mmapped_file.readline().decode().strip()
        node, value = [int(x) for x in line.strip().split("\t")]

        if node not in data:
            data[node] = []
            G.add_node(node) 

        data[node].append(value)
        G.add_edge(node,  value)

        if(value > n):
            n = value
    else : 
     for line in mmapped_file:
        line = mmapped_file.readline().decode().strip()
        node, value = [int(x) for x in line.strip().split("\t")]

        if node not in data:
            data[node] = []
            G.add_node(node) 

        data[node].append(value)
        G.add_edge(node,  value)

        if(value > n):
            n = value

print("\nstarting to initialize the graph\n\n")

graph = BidirectionalSearch(n+1)

print("adding the data in the graph data structure ...\n\n")
for node, edges in data.items():
    for edge in edges:
        graph.add_edge(node, edge)


node_colors = ['blue' for node in G.nodes()]

print("beging the search from the source : %i and from the gaol : %i ...\n\n"%(src,dest))

graph.bidirectional_search(src,dest)
