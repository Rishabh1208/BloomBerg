# Recursion with memoization
def uniquePaths(m, n):

    dp = [[-1 for i in range(n)] for j in range(m)]

    def helper(i, j):

        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = helper(i-1, j)
        left = helper(i, j-1)

        dp[i][j] = up + left

        return dp[i][j]

    return helper(m-1, n-1)


m = 3
n = 7
print(uniquePaths(m, n))

# Tabulation


def uniquePaths(m, n):

    dp = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[m-1][n-1]


m = 3
n = 7
print(uniquePaths(m, n))

# space optimization with O(N) space ( this is not working in leetcode somehow but the solution is correct)

def uniquePaths(m, n):
    prev = [0 for i in range(n)]

    for i in range(m):
        temp = [0 for i in range(n)]
        for j in range(n):
            if i == 0 and j == 0:
                temp[j] = 1
            else:
                up = prev[j] if i > 0 else 0
                left = temp[j-1] if j > 0 else 0
                temp[j] = up + left

        prev = temp

    return prev[n-1]


m = 3
n = 7
print(uniquePaths(m, n))
