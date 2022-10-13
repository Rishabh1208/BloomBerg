# Definition for a binary tree node.
from collections import defaultdict
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getCoordinates(self, root, x, y, coordinates):
        if not root:
            return coordinates

        coordinates.append([x, y, root.val])
        self.getCoordinates(root.left, x-1, y-1, coordinates)
        self.getCoordinates(root.right, x+1, y-1, coordinates)

        return coordinates

    def verticalTraversal(self, root):
        if not root:
            return []

        coordinates = self.getCoordinates(root, 0, 0, [])
        # why we are sorting like this?
        coordinates.sort(key=lambda x: (x[0], -x[1], x[2]))
        # Look at these examples:
        # For x[0] look at example given in the leetcode.
        # Inout: [3,1,4,0,2,2] output: [[0],[1],[3,2,2],[4]] --> This is for -x[1]
        # Input: [3,1,4,0,2,5] output: [[0],[1],[3,2,5],[4]] --> This is for x[2]

        result = [[coordinates[0][2]]]
        for i in range(1, len(coordinates)):
            if coordinates[i][0] == coordinates[i-1][0]:
                result[-1].append(coordinates[i][2])
            else:
                result.append([coordinates[i][2]])
        return result


# O(NlogN)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode):
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]

# o(N)
def verticalOrder(root):
    if root is None:
        return []

    columnTable = defaultdict(list)
    min_column = max_column = 0
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()

        if node is not None:
            columnTable[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

    return [columnTable[x] for x in range(min_column, max_column + 1)]
