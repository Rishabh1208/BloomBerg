
# For Union Find remember 3 Things
# 1) FindParent()
# 2) FindRank()
# 3) Path compression while finding parent.

def findRedundantConnection(self, edges):
    parent = [i for i in range(len(edges)+1)]
    rank = [0] * (len(edges) + 1)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(u, v):
        p1, p2 = find(u), find(v)

        if p1 == p2:
            return True

        if rank[p1] == rank[p2]:
            parent[p2] = p1
            rank[p1] += 1

        if rank[p1] > rank[p2]:
            parent[p2] = p1

        else:
            parent[p1] = p2

    for u, v in edges:
        if union(u, v):
            return [u, v]
