#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj, rev_adj):
    result = 0
    #write your code here
    postorder = []
    visited = [False]*len(adj)
    cc = []
    component_now = []

    def explore(v):
        visited[v] = True
        for w in rev_adj[v]:
            if not visited[w]:
                explore(w)
        postorder.append(v)

    def scc_explore(v):
        visited[v] = True
        component_now.append(v)
        for w in adj[v]:
            if not visited[w]:
                scc_explore(w)
        

    for i in range(len(adj)):
        if not visited[i]:
            explore(i)

    #print(postorder)

    visited = [False]*len(adj)
    while postorder:
        v = postorder.pop()
        if not visited[v]:
            scc_explore(v)
        if component_now: cc.append(component_now)
        component_now = []

    #print(cc)
    result = len(cc)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev_adj[b-1].append(a-1)
    print(number_of_strongly_connected_components(adj, rev_adj))
