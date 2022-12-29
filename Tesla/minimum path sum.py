def minPathSum(self, grid):
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
