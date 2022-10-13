

from collections import defaultdict


def findOrder(numCourses, prerequisites):
    result = []
    # preMap = defaultdict(list) # This is another way to create adjacency list.
    preMap = {i: [] for i in range(numCourses)}  # create adjacency list.
    for u, v in prerequisites:
        preMap[u].append(v)

    visited = set()  # if we have already visited the node before.
    # if in currenly dfs cycle, if we have visisted that node earlier.
    cycle = set()

    def dfs(i):
        if i in cycle:
            return False

        if i in visited:
            return True

        cycle.add(i)
        for j in preMap[i]:
            if not dfs(j):
                return False

        cycle.remove(i)
        visited.add(i)
        result.append(i)

        return True

    for i in range(numCourses):
        if not dfs(i):
            return []

    return result


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(numCourses, prerequisites))


# In this solution, the only difference is we are not taking 2 sets, in one set only we are checking.
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # use DFS to parse the course structure
        self.graph = defaultdict(list)  # a graph for all courses
        self.res = []  # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.visited = [0 for x in range(numCourses)]  # DAG detection
        for x in range(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res

    def DFS(self, node):
        if self.visited[node] == -1:  # cycle detected
            return False
        if self.visited[node] == 1:
            return True  # has been finished, and been added to self.res
        self.visited[node] = -1  # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1  # mark as finished
        # add to solution as the course depenedent on previous ones
        self.res.append(node)
        return True
