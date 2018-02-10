#Uses python3
import sys
import math
import sys
import math

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
        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


def clustering(x, y, k):
    #write your code here

    points = list(zip(x,y))
    n = len(points)
    cluster = n
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            edges.append((dist, i, j))

    edges = sorted(edges, key = lambda x: x[0])
    #print(edges)

    uf = UnionFind(n)

    for edge in edges:
        d, x, y = edge[0], edge[1], edge[2]
        if not uf.find(x, y) and cluster > k:
            uf.union(x, y) 
            cluster -= 1
        if cluster == k and not uf.find(x, y):
            return edges[edges.index(edge)][0]
            break
    
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
