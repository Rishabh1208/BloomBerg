# Recursion with memoization
def minPathSum(grid):
    r = len(grid)
    c = len(grid[0])

    dp = [[-1 for i in range(c)] for j in range(r)]

    def helper(i, j):
        if i < 0 or j < 0:
            return float('inf')

        if i == 0 and j == 0:
            return grid[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

        up = grid[i][j] + helper(i-1, j)
        left = grid[i][j] + helper(i, j-1)

        dp[i][j] = min(up, left)

        return dp[i][j]

    return helper(r-1, c-1)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))

# Tabulation


def minPathSum(grid):
    r = len(grid)
    c = len(grid[0])

    dp = [[-1 for i in range(c)] for j in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                up = grid[i][j] + dp[i-1][j] if i > 0 else float('inf')
                left = grid[i][j] + dp[i][j-1] if j > 0 else float('inf')

                dp[i][j] = min(up, left)

    return dp[r-1][c-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))
