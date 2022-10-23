def maxPathSum(self, root):
    maxPath = [float("-inf")]

    # return max path without split
    def dfs(root):
        if root is None:
            return 0

        leftSubTree = max(dfs(root.left), 0)
        rightSubTree = max(dfs(root.right), 0)

        # compue the max path sum with split
        maxPath[0] = max(maxPath[0], leftSubTree + rightSubTree + root.val)

        return root.val + max(leftSubTree, rightSubTree)

    print(dfs(root))
    return maxPath[0]
