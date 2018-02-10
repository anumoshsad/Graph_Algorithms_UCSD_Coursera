#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    distance[s] = 0
    reachable[s] = 1

    q = queue.Queue()
    for _ in range(len(adj)-1):
        for u in range(len(adj)):
            for v in adj[u]:
                if distance[v] > distance[u] + cost[u][v]:
                    distance[v] = distance[u] + cost[u][v]
                    reachable[v] = 1

    for u in range(len(adj)):
        for v in adj[u]:
            if distance[v] > distance[u] + cost[u][v]:
                q.put(v)

    while not q.empty():
        u = q.get()
        shortest[u] = 0
        for v in adj[u]:
            if shortest[v] == 1:
                q.put(v)
                
    return

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [{} for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1][b-1] = w
    s = data[0]
    s -= 1
    distance = [float("inf")] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

