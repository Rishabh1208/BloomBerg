def allPathsSourceTarget(graph):
    res = []

    def dfs(node, path):
        if node == len(graph)-1:
            res.append(path[:])
            return

        for n in graph[node]:
            path.append(n) # This is change
            dfs(n, path)
            path.pop()

    dfs(0, [0]) # This is change
    return res

# This is derived by me, it is almost same but the only difference I can see is I am not adding
# [0] to the path initially.
def allPathsSourceTarget(graph):
    res = []

    def dfs(i, path):
        path.append(i) # This is change

        if i == len(graph)-1:
            res.append(path[:])
            return

        for j in graph[i]:
            dfs(j, path)
            path.pop()

    dfs(0, []) # This is change
    return res
