# Recursive
def inorderTraversal(self, root):
    result = []

    def dfs(root):
        if root is None:
            return None
        dfs(root.left)
        result.append(root.val)
        dfs(root.right)

    dfs(root)
    return result


# iteratively
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
