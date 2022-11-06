def findTargetSumWays(self, nums, target):
    total = sum(nums)
    diff = total - target
    if diff < 0 or diff % 2 == 1:
        return 0
    targ = diff // 2

    def dfs(i, tar):

        if i == 0:
            if nums[i] == 0 and tar == 0:
                return 2
            if nums[i] == tar or tar == 0:
                return 1
            return 0

        notPick = dfs(i-1, tar)
        pick = 0
        if tar >= nums[i]:
            pick = dfs(i-1, tar-nums[i])
        return notPick + pick

    return dfs(len(nums)-1, targ)
