def graphValidTree(n, edges):
    preMap = {i: [] for i in range(n)}

    for u, v in edges:
        preMap[u].append(v)
        preMap[v].append(u)

    print("preMap", preMap)

    visited = set()

    def dfs(node, prev):
        if node in visited:
            return False

        visited.add(node)

        for i in preMap[node]:
            if i == prev:
                continue
            if not dfs(i, node):
                return False

        return True

    return dfs(0, -1)


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

print(graphValidTree(n, edges))
