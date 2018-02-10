#Uses python3

import sys
ans = 0

def acyclic(adj):
    visited = [False]*len(adj)
    stack = []

    def explore(v):
        global ans
        stack.append(v+1)
        #print(stack)
        visited[v] = True
        for w in adj[v]:
            if w+1 in stack: 
         #       print(w+1)
                ans = 1
                return
            if not visited[w] and ans == 0:
                explore(w)
        stack.pop()
        return

    for i in range(len(adj)):
        if not visited[i]:
            explore(i)
            #print(ans)
            if ans ==1:
                return 1
    
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
