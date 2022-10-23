def findWays(num, target):
    memo = [[-1 for i in range(target+1)] for j in range(len(nums))]

    def dfs(i, target):

        if target < 0:
            return 0

        if i == 0:
            if num[i] == 0 and target == 0:
                return 2
            if target == 0 or nums[i] == target:
                return 1
            return 0

        # remove this if nums[i] >=0
        # if target == 0:
        #     return 1

        # remove this if nums[i] >=0
        # if i == 0:
        #     if num[i] == target:
        #         return 1
        #     else:
        #         return 0

        if memo[i][target] != -1:
            return memo[i][target]

        notPick = dfs(i-1, target)
        pick = dfs(i-1, target-num[i])

        memo[i][target] = pick + notPick
        print("memo", memo)

        return memo[i][target]

    return dfs(len(num)-1, target)


# we are taking this into consideration that nums[i] >=1 but what if it is
# nums = [1, 2, 2, 3]
# nums[i] >=0 For Example: [0,0,1] and target = 1. , output would be 4 --> [0,1] [0,1] [0,0,1] [1]
# target = 3

nums = [0, 0, 1]
target = 1
print(findWays(nums, target))
