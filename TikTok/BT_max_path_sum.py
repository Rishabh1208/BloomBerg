# Brute-force - O(N^2)
# Better Approach - o(N)
# we start from the bottom and do it like post order traversal.
def maxPathSum(self, root):
    maxPath = [float("-inf")]

    # return max path without split
    def dfs(root):
        if root is None:
            return 0
        # if we get any negative value from either a left sub tree or right sub tree
        # instead of returning the negative value, I would return 0 because 
        # we are calculating a max path sum. for eg - 10 - 5 = 5 instead 10 - 0 =10
        leftSubTree = max(dfs(root.left), 0)
        rightSubTree = max(dfs(root.right), 0)

        # compue the max path sum with split
        maxPath[0] = max(maxPath[0], leftSubTree + rightSubTree + root.val)

        return root.val + max(leftSubTree, rightSubTree)

    dfs(root)
    return maxPath[0]
