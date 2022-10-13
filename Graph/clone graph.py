
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.neighbors = [Node]


def cloneGraph(self, node):
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None
