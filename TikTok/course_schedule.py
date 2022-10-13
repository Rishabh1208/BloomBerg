# numCourses = 2, prerequisites = [[1,0]]
# Time and space complexity: O(E+V)
# course schedule is same as detecting cycle in a directed graph.
def canFinish(self, numCourses, prerequisites):
    # map each course to prrreq list
    preMap = {i: [] for i in range(numCourses)}

    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # visitSet = all courses along the curr DFS path
    visitSet = set()

    def dfs(crs):
        if crs in visitSet:
            return False
        # if there is no prereq for this course, it will return True
        if preMap[crs] == []:
            return True

        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        # since we already visited we have to remove this from our visited set
        visitSet.remove(crs)
        preMap[crs] = []
        return True

    # Reason why we are using for loop. because there might be chances the graph is not connected for eg- [1,2] [3,4]
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True
