# https://leetcode.com/discuss/interview-question/1013880/Bloomberg-or-Phone-%2B-Onsite-or-Interview-Questions


# https://leetcode.com/discuss/interview-question/550259/bloomberg-phone-interview-se-grad-2020


# 'm' amount of oil can be purchased from 'n' companies. Every company has 'k' capacity of oil to be sold, 
# you can take zero or many times the quantity offered by each company. Give the maximum number of combinations possible.

# For examples:
# There are three companies: A, B, C

# A - 10
# B - 15
# C - 50

# Target: 60

# Number of Combinations: 4 {[10,50], [15,45], [20,40],[10,20,30]

# combination sum and coin change 2
def combinations(nums, target):

    def dfs(i, target):
        if target == 0:
            return 1

        if i == 0:
            if target % nums[i] == 0:
                return 1
            else:
                return 0

        notPick = dfs(i-1, target)
        pick = 0
        if nums[i] <= target:
            pick = dfs(i, target - nums[i])
        return notPick + pick

    return dfs(len(nums)-1, target)


nums = [10, 15, 50]
target = 60

print(combinations(nums, target))
