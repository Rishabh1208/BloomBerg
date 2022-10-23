import collections

# equations = [["a","b"],["b","c"]], values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

# DFS


def calcEquation(equations, values, queries):
    # Step 1. Build the Graph
    graph = collections.defaultdict(dict)
    for (x, y), val in zip(equations, values):
        graph[x][y] = val
        graph[y][x] = 1.0 / val
    print(graph)

    # Step 2. DFS function
    def dfs(x, y, visited):
        # neither x not y exists
        if x not in graph or y not in graph:
            return -1.0

        # x points to y
        if y in graph[x]:
            return graph[x][y]

        # x maybe connected to y through other nodes
        # use dfs to see if there is a path from x to y
        for i in graph[x]:
            if i not in visited:
                visited.add(i)
                temp = dfs(i, y, visited)
                if temp == -1:
                    continue
                else:
                    return graph[x][i] * temp
        return -1

    # go through each of the queries and find the value
    res = []
    for query in queries:
        res.append(dfs(query[0], query[1], set()))
    return res

# BFS

def calcEquation(self, equations, values, queries):

    graph = {}

    def build_graph(equations, values):
        def add_edge(f, t, value):
            if f in graph:
                graph[f].append((t, value))
            else:
                graph[f] = [(t, value)]

        for vertices, value in zip(equations, values):
            f, t = vertices
            add_edge(f, t, value)
            add_edge(t, f, 1/value)

    def find_path(query):
        b, e = query

        if b not in graph or e not in graph:
            return -1.0

        q = collections.deque([(b, 1.0)])
        visited = set()

        while q:
            front, cur_product = q.popleft()
            if front == e:
                return cur_product
            visited.add(front)
            for neighbor, value in graph[front]:
                if neighbor not in visited:
                    q.append((neighbor, cur_product*value))

        return -1.0

    build_graph(equations, values)
    return [find_path(q) for q in queries]
