#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #write your code here
    flag = [False]*len(adj)
    dist = [float("inf")]*len(adj)
    prev = [None]*len(adj)
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0,s))
    flag[s] = True
    while not pq.empty():
        while not pq.empty():
            (dis, u) = pq.get()
            if flag[u]:
                flag[u] = False
                break

        for v in range(len(adj[u])):
            if dist[adj[u][v]] > dist[u] + cost[u][v]:
                dist[adj[u][v]] = dist[u] + cost[u][v]
                prev[adj[u][v]] = u
                pq.put((dist[adj[u][v]], adj[u][v]))
                flag[adj[u][v]] = True
                prev[adj[u][v]]=u      
        #print(pq.queue)
    if dist[t] < float("inf"):
        return dist[t] 
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
