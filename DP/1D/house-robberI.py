# Recursion
def rob(nums):
    n = len(nums)

    def helper(idx):

        if idx == 0:
            return nums[idx]
        if idx < 0:
            return 0

        pick = nums[idx] + helper(idx-2)
        notPick = helper(idx-1)

        return max(notPick, pick)

    return helper(n-1)


nums = [1, 2, 3, 1]
print(rob(nums))

# Recursion with memoization (Top Bown)
def rob(nums):
    n = len(nums)
    dp = [-1 for i in range(n)]

    def helper(idx):
        if idx < 0:
            return 0

        if idx == 0:
            return nums[idx]

        if dp[idx] != -1:
            return dp[idx]

        notPick = helper(idx-1)
        pick = nums[idx] + helper(idx-2)

        dp[idx] = max(notPick, pick)

        return dp[idx]

    return helper(n-1)


nums = [1, 2, 3, 1]
print(rob(nums))

# Tabulation with O(N) space without recursion stack (Bottom Up)
def rob(nums):
    n = len(nums)
    dp = [-1 for i in range(n)]

    dp[0] = nums[0]
    for idx in range(1, n):
        notPick = dp[idx-1]
        pick = nums[idx]
        if idx > 1:
            pick += dp[idx-2]

        dp[idx] = max(notPick, pick)
    return dp[n-1]


nums = [1, 2, 3, 1]
print(rob(nums))

# Tabulation with O(1) space
def rob(nums):
    n = len(nums)
    prev1 = nums[0]
    prev2 = 0 # for negative index
    for idx in range(1, n):
        notPick = prev1
        pick = nums[idx]
        if idx > 1:
            pick += prev2

        curr = max(notPick, pick)
        prev2 = prev1
        prev1 = curr
    return prev1


nums = [1, 2, 3, 1]
print(rob(nums))
