# Definition for a binary tree node.
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
        coordinates.sort(key=lambda x: (x[0], -x[1], x[2])) # why we are sorting like this?
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
