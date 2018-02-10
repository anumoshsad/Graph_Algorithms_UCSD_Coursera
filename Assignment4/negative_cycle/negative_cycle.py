#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    dist = [float("inf")]*len(adj)
    dist[n] = 0
    for _ in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                dist[v] = min(dist[v], dist[u] + cost[u][v])
    for u in range(len(adj)):
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][v]:
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n+1)]
    cost = [{} for _ in range(n+1)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1][b-1] = w
    for i in range(n):
        adj[n].append(i)
        cost[n][i] = 0
    print(negative_cycle(adj, cost))
