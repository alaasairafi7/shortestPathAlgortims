import matplotlib.pyplot as plt
import networkx as nx
import mmap
import time

nodes = []

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def search(self, value):
        if self.root is None:
            return False
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def visualize(self):
        G = nx.Graph()

        self._visualize(self.root, G)

        pos = nx.spring_layout(G)
    

        labels = nx.get_node_attributes(G, 'value')

        nx.draw_networkx_nodes(G,pos, node_color='blue' , node_size=30)
        nx.draw_networkx_edges(G, pos, width=0.5)
        nx.draw_networkx_labels(G, pos, labels)
        plt.show()

    def _visualize(self, node, G, parent=None):
        if node is not None:
            G.add_node(node)
            G.nodes[node]['value'] = node.value
            if parent is not None:
                G.add_edge(parent, node)
            self._visualize(node.left, G, node)
            self._visualize(node.right, G, node)

 
class BidirectionalSearch:
    def __init__(self, start, end, tree):
        self.start = start
        self.end = end
        self.tree = tree
        self.path_from_start = []
        self.path_from_end = []

    def search(self):
        start_time = time.perf_counter()#for caculate the time
#code to calulate
        start_node = self.tree.root
        end_node = self.tree.root

        if(tree.search(self.start) and tree.search(self.end)):

         while start_node is not None:
            if start_node.value == self.start:
                break
            elif start_node.value > self.start:
                self.path_from_start.append(start_node.value)
                start_node = start_node.left
            else:
                self.path_from_start.append(start_node.value)
                start_node = start_node.right

         while end_node is not None:
            if end_node.value == self.end:
                break
            elif end_node.value > self.end:
                self.path_from_end.append(end_node.value)
                end_node = end_node.left
            else:
                self.path_from_end.append(end_node.value)
                end_node = end_node.right

         if(self.path_from_start != []):
          for value in self.path_from_start[::-1]:
           if value != self.end :
             if value in self.path_from_end:
                common_ancestor = value

                path_list = list()

                for l in [[node for node in self.path_from_start][::-1],[node for node in self.path_from_end][::-1]]:
                 index = l.index(common_ancestor)+1
                 path_list += [l[i:i + index] for i in range(0, len(l), index)][0]

                path_list.pop()
                path_list.insert(0, self.start)
                path_list.append(self.end)
                
                path_list = list(map(str, path_list))
         

                print(f"\n\nPath exists between {self.start} and {self.end}")

                print(f"\n\nIntersection at : {common_ancestor}")

                print("\n\npath :", ' -> '.join(path_list))

                

                tree.visualize()

                exit(0)
           else : 
                common_ancestor = self.end
                path_list = list()

                l = [node for node in self.path_from_start][::-1]
                index = l.index(common_ancestor)+1

                path_list = [l[i:i + index] for i in range(0, len(l), index)][0]

                path_list.insert(0, self.start)
                
                path_list = list(map(str, path_list))
         

                print(f"\n\nPath exists between {self.start} and {self.end}")

                print(f"\n\nIntersection at : {common_ancestor}")

                print("\n\npath :", ' -> '.join(path_list))

                

                tree.visualize()

                exit(0)
         else:
                common_ancestor = self.start

                path_list = list()

                path_list =  self.path_from_end
                path_list.append(self.end)
                
                path_list = list(map(str, path_list))  

                print(f"\n\nPath exists between {self.start} and {self.end}")

                print(f"\n\nIntersection at : {common_ancestor}")

                print("\n\npath :", ' -> '.join(path_list))

                end_time = time.perf_counter()#for caculate the time
                        
                print("time=",end_time-start_time)

                tree.visualize()

                exit(0)

        else :

         print(f"Path does not exist between {self.start} and {self.end} because one or the two of them are not in the tree ")

         print("\n\nvisualizing the graph ... ")

         tree.visualize()



    

        print(f"Path does not exist between {self.start} and {self.end}")

        print("\n\nvisualizing the graph ... ")

        tree.visualize()

        
            


print("\nstarting to initialize the tree\n\n")

data_path = "/Users/NADIA.AKBER/Downloads/testnetwork.txt"


#this is the max number of lines that the program will read from the datafile because it is so big ,
#however you can get all the data if you want if you made "Get_all_data" = True

Get_all_data = False

number_of_lines_to_get_from_the_data_file = 100


tree = BinarySearchTree()

src = 12

dest = 53

print("adding the data from file to the tree data structure ...\n\n")

with open(data_path, "r") as file:

    mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

    if(not Get_all_data):

     for line in range(number_of_lines_to_get_from_the_data_file):
        line = mmapped_file.readline().decode().strip()
        data1, data2 = [int(x) for x in line.strip().split("\t")]
        if not tree.search(data1) :
           nodes.append(data1)
           tree.insert(data1)
        tree.insert(data2)
        nodes.append(data2)

    else :
        
     for line in mmapped_file :
        line = mmapped_file.readline().decode().strip()
        data1, data2 = [int(x) for x in line.strip().split("\t")]
        if not tree.search(data1) :
           nodes.append(data1)
           tree.insert(data1)
        tree.insert(data2)
        nodes.append(data2)


print("beging the search from the source : %i and from the gaol : %i ...\n\n"%(src,dest))

BidirectionalSearch(src,dest,tree).search()

tree.visualize()