def isBalanced(self, root):
    # returning 2 different things that is array[balanced, height] - To improve the
    # time complexity
    def dfs(root):
        if root is None:
            return [True, 0]
        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]
    return dfs(root)[0]
