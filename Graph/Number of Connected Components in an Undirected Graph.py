class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return

        if self.rank[p2] > self.rank[p1]:
            pass

        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = self.parent[p1]

        else:
            self.parent[p2] = p1
            self.rank[p1] += 1


def countComponents(n, edges):
    ds = DSU(n)
    for n1, n2 in edges:
        ds.union(n1, n2)
        print(n1, n2,  ds.parent, ds.rank)

    parent = set(ds.parent)
    return len(parent)


n = 5
edges = [[0, 1], [1, 2], [3, 4]]

print(countComponents(n, edges))
