def climbStairs(self, n):
    dp = {}
    dp[0] = 1

    def dfs(n):
        if n < 0:
            return 0
        if n in dp:
            return dp[n]
        one = dfs(n-1)
        two = dfs(n-2)
        dp[n] = one + two
        return dp[n]
    return dfs(n)
