def hasPathSum(self, root, targetSum):
    if root is None:
        return False
    if not root.left and not root.right and root.val == targetSum:
        return True
    return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
