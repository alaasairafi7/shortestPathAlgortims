
from queue import PriorityQueue
import time
start = time.process_time() 
n = 5000
graph = [[] for i in range(n)]

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 
def get_line():
     with open('test.txt') as file:
         for i in file:
             yield i
pq = PriorityQueue()
lines_required = 5000
gen = get_line()
chunk = [i for i, j in zip(gen, range(5000))]
for i in chunk:
    tmp = i.split()
    a = int(tmp[0])
    b = int(tmp[1].replace('\n','').replace('q',''))
    w=int(tmp[2].replace('\n','').replace('q',''))
    addedge(a,b,w)
   
 
# Function For Implementing Best First Search
# Gives output path having lowest cost
 
print('\n')
def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
     
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break
 
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
 
source = 1
target = 5
best_first_search(source, target, n)
print('\nprocess time=', time.process_time() - start)  