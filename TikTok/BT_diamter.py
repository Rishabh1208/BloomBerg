# Brute force - For every node, we calculate the height and diameter and update the res.
# Time complexity - o(N^2)
# Better approach - calculate the height and diameter while traversing the first time. and start from
# bottom to top.
# Time complexity - o(N)
def diameterOfBinaryTree(self, root):
    res = [0]  # global variable.
    # res = 0
    def dfs(root):
        # nonlocal res
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
