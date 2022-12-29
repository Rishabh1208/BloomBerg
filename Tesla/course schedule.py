

from collections import defaultdict


def findOrder(numCourses, prerequisites):

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

        return True

    for i in range(numCourses):
        if not dfs(i):
            print(i, False)
            return False

    # if you don't return anything from dfs by default it will return None and that means False.
    return True


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# prerequisites = [[0,1],[1,0]]
print(findOrder(numCourses, prerequisites))


def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
