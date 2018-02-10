#Uses python3
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


def minimum_distance(x, y):
    result = 0.
    #write your code here
    points = list(zip(x,y))
    n = len(points)
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
    	if not uf.find(x, y):
    		result += d
    		uf.union(x, y) 

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
