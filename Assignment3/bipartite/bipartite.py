#Uses python3

import sys
from collections import deque

def bipartite(adj):
    #write your code here
    n = len(adj)
    visited = [0]*n
    parent = [0]*n
    
    for i in range(len(adj)):
        if visited[i] == 0:
            visited[i]=1
            q = deque([i])
            while q:
                v = q.popleft()
                
                for w in adj[v]:
                    if visited[w] == 0:
                        q.append(w)
                        visited[w]= - visited[v]
                       # print(q, visited)
                    if visited[v] == visited[w]:
                        return 0
        
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
