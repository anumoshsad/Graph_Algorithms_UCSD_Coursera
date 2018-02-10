#Uses python3

import sys

class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.sz = [1]*n
        self.components = n


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
        if i!=j: self.components -= 1
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]

        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

def number_of_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    uf = UnionFind(n)
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        uf.union(a-1, b-1)
    print(uf.components)
