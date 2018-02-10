#Uses python3

import sys

class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.sz = [1]*n


    def root(self, i):
        j = i
        while j != self.id[j]:
            self.id[j] = self.id[self.id[j]]
            j = self.id[j]
        return j

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]

        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]



def reach(adj, x, y):
    #write your code here
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1

    uf = UnionFind(n)
    for (a, b) in edges:
        uf.union(a-1,b-1)
        #print(uf.id)

    print(1 if uf.find(x,y) else 0)
