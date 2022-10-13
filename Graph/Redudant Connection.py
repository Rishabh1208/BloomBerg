
# For Union Find remember 3 Things
# 1) FindParent()
# 2) FindRank()
# 3) Path compression while finding parent.

def findRedundantConnection(edges):
    parent = [i for i in range(len(edges)+1)]
    rank = [1] * (len(edges)+1)

    def find(n):
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]  # Path compression
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]

        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]
