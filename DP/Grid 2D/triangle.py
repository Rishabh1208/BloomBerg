# Recursion with memoization
def minimumTotal(triangle):
    r = len(triangle)
    c = len(triangle[r-1])

    dp = [[-1 for i in range(c)] for j in range(r)]

    def helper(i, j):
        if i == r-1:
            return triangle[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

        down = triangle[i][j] + helper(i+1, j)
        diag = triangle[i][j] + helper(i+1, j+1)

        dp[i][j] = min(down, diag)

        return dp[i][j]

    return helper(0, 0)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimumTotal(triangle))

# Tabulation
def minimumTotal(triangle):
    r = len(triangle)
    c = len(triangle[r-1])

    dp = [[-1 for i in range(c)] for j in range(r)]

    for i in range(r):
        dp[r-1][i] = triangle[r-1][i]

    for i in range(r-2, -1, -1):
        for j in range(i, -1, -1):
            down = triangle[i][j] + dp[i+1][j]
            diag = triangle[i][j] + dp[i+1][j+1]

            dp[i][j] = min(down, diag)
    return dp[0][0]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimumTotal(triangle))

#Tabulation with o(1) space
