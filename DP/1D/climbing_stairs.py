
# Recursion with memoization
def climbStairs(n):
    dp = [-1 for i in range(n+1)]

    def helper(idx):
        if idx == 0:
            return 1
        if idx == 1:
            return 1
        if dp[idx] != -1:
            return dp[idx]
        firstStep = helper(idx-1)
        secondStep = helper(idx-2)

        dp[idx] = firstStep + secondStep
        return dp[idx]

    return helper(n)


n = 3
print(climbStairs(n))

# Tabulation
def climbStairs(n):
    dp = [-1 for i in range(n+1)]

    dp[0] = 1
    dp[1] = 1
    for idx in range(2, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]

    return dp[n]


n = 3
print(climbStairs(n))

# Tabulation with o(1) space
def climbStairs(n):

    prev2 = 1
    prev1 = 1
    for idx in range(2, n+1):
        curr = prev2 + prev1
        prev2 = prev1
        prev1 = curr

    return prev1


n = 3
print(climbStairs(n))
