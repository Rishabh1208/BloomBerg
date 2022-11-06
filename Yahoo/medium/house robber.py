def rob(self, nums):
    memo = {}
    memo[0] = nums[0]

    def dfs(i):

        if i < 0:
            return 0

        if i in memo:
            return memo[i]

        # if i == 0:
        #     return nums[i]

        memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
        return memo[i]

    return dfs(len(nums)-1)
