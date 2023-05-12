
from queue import PriorityQueue
import time
start_time = time.perf_counter()
v = 5000

GRAPH = [[0 for i in range(5000)] for j in range(5000)]

def loadGraph():
    
    my_file = open("test.txt", "r")
    for number in my_file:
        nums=number.split("\t")
        row=int(nums[0])-1
        col=int(nums[1].strip())-1
        GRAPH[row][col]=float(nums[2].strip())
loadGraph()
pq = PriorityQueue()
 
# Function For Implementing Best First Search
# Gives output path having lowest cost
 
from queue import PriorityQueue
def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
    print('\n')
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break
        for v in range(len(GRAPH[u])):
            c=GRAPH[u][v]
            if c!=0:
               if visited[v] == False:
                 visited[v] = True
                 pq.put((c, v))
    print()

source = 1
target = 5
best_first_search(source, target, v)
end_time = time.perf_counter()
print('\nprocess time=', end_time-start_time)