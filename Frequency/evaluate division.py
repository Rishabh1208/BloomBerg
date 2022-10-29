import collections

# equations = [["a","b"],["b","c"]], values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

# DFS


def calcEquation(equations, values, queries):

    graph = collections.defaultdict(dict)

    def backtrack_evaluate(curr_node, target_node, acc_product, visited):
        visited.add(curr_node)
        ret = -1.0
        neighbors = graph[curr_node]
        if target_node in neighbors:
            ret = acc_product * neighbors[target_node]
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ret = backtrack_evaluate(
                    neighbor, target_node, acc_product * value, visited)
                if ret != -1.0:
                    break
        visited.remove(curr_node)
        return ret

    # Step 1). build the graph from the equations
    for (dividend, divisor), value in zip(equations, values):
        # add nodes and two edges into the graph
        graph[dividend][divisor] = value
        graph[divisor][dividend] = 1 / value

    # Step 2). Evaluate each query via backtracking (DFS)
    #  by verifying if there exists a path from dividend to divisor
    results = []
    for dividend, divisor in queries:
        if dividend not in graph or divisor not in graph:
            # case 1): either node does not exist
            ret = -1.0
        elif dividend == divisor:
            # case 2): origin and destination are the same node
            ret = 1.0
        else:
            visited = set()
            ret = backtrack_evaluate(dividend, divisor, 1, visited)
        results.append(ret)

    return results


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
