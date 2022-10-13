# Find cycle in undirected graph.
def validTree(n, edges):
    if not n:
        return True

    adj = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visit = set()

    def dfs(i, prev):
        if i in visit:
            return False

        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True

    return dfs(0, -1) and n == len(visit)


def validTree(n, edges):
    if n - 1 != len(edges):
        return False
    # initialize a parent array where each vertex belongs to itself
    parent = [i for i in range(n)]

    # find operation
    def find(v):
        if parent[v] != v:
            # use path compression to gain some time
            parent[v] = find(parent[v])
        return parent[v]

    for edge in edges:
        # for each edge, check if two vertices belongs to one set
        # if yes then a cycle is found
        set1 = find(edge[0])
        set2 = find(edge[1])
        if set1 == set2:
            return False

        # union
        parent[set1] = set2

    return True
