# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]  # global variable.

        def dfs(root):
            if root is None:
                # we are returning the height, if there is no node, we would be returning -1.
                return -1
            left = dfs(root.left)  # leftHeight
            right = dfs(root.right)  # rightHeight
            # updating the res (that is current max diamater)
            res[0] = max(res[0], left + right + 2)
            return 1 + max(left, right)

        dfs(root)
        return res[0]
