# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def findBottomLeftValue(self, root):
        q = deque([root])
        node = None
        while q:
            # In Python variable is function scoped not block scope
            node = q.popleft()

            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

        return node.val
