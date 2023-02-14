from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)
    if rootx != rooty:
        if rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        elif rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        else:
            parent[rooty] = rootx
            rank[rootx] += 1

def minCostConnecting(n, router, ethernet):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    edges = [(i, i, cost) for i, cost in enumerate(router)]
    for a, b, cost in ethernet:
        edges.append((a, b, cost))
    edges.sort(key=lambda x: x[2])
    cost = 0
    for a, b, c in edges:
        if find(parent, a) != find(parent, b):
            cost += c
            union(parent, rank, a, b)
    return cost

n = 10
router = [13, 19, 15, 14, 9, 6, 12, 11, 18, 12]
ethernet = [[6,7,2], [5,6,18], [2,5,2], [0,1,6], [7,9,3], [1,2,6], [4,9,20]]
print(minCostConnecting(n, router, ethernet))

