# https://leetcode.com/problems/all-paths-from-source-to-target/
# [The given graph can have cycles though]

# Example - (1,5),(2,7),(11,18) --> Ans: (11,18),(2,7) You skip the (1,5) interval
# since you have already chosen the (2,7) interval. The tricky/corner cases were hard
# to manage, for example when you have (8,9) in the list as well. I came up with a O(n2)
# solution which the interviewer said that's what they expected but the optimized way of
# doing this was through graphs (Dint have time to discuss the graph approach)

# And what was the hint for managing the cycles? --> Instead of having a global visited set,
# maintain a local visited set for each. So I used BFS, and I had a tuple of 3 items :
# (node, path_to_node, local_visited). I used this approach and the interviewer seemed satisfied.

def allPathsSourceTarget(graph):
    res = []

    def dfs(node, path):
        if node == len(graph)-1:
            res.append(path[:])
            return

        for n in graph[node]:
            path.append(n)  # This is change
            dfs(n, path)
            path.pop()

    dfs(0, [0])  # This is change
    return res

# This is derived by me, it is almost same but the only difference I can see is I am not adding
# [0] to the path initially.


def allPathsSourceTarget(graph):
    res = []

    def dfs(i, path):
        path.append(i)  # This is change

        if i == len(graph)-1:
            res.append(path[:])
            return

        for j in graph[i]:
            dfs(j, path)
            path.pop()

    dfs(0, [])  # This is change
    return res

# with cycles.
def allPathsSourceTarget(graph):
    res = []

    visited = set()

    def dfs(node, path):

        if node == len(graph)-1:
            res.append(path[:])
            return

        visited.add(node)

        for n in graph[node]:
            if n not in visited:
                path.append(n)
                dfs(n, path)
                path.pop()
        visited.remove(node)

    dfs(0, [0])
    return res


graph = [[4, 1], [3, 2, 4], [3], [4, 0], []]
print(allPathsSourceTarget(graph))
