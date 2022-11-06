def uniquePaths(self, m, n):
    memo = [[-1 for j in range(n)] for i in range(m)]  # List comprehension
    memo[0][0] = 1

    def dfs(m, n):
        if memo[m][n] != -1:
            return memo[m][n]

        up = m > 0 and dfs(m-1, n)
        left = n > 0 and dfs(m, n-1)

        memo[m][n] = up + left
        return memo[m][n]

    return dfs(m-1, n-1)
