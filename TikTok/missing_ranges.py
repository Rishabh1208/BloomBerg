def findMissingRanges(self, nums, lower, upper):
    #  the only part is adding lower-1 to nums will iterate nums once so O(n) will become O(2n)
    nums = [lower-1] + nums + [upper+1]
    res = []

    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 2:
            res.append(str(nums[i]+1))
        elif nums[i+1] - nums[i] > 2:
            res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))

    return res


def findMissingRanges(self, nums, lower, upper):
    result = []
    nums.append(upper+1)
    pre = lower - 1
    for i in nums:
        if (i == pre + 2):
            result.append(str(i-1))
        elif (i > pre + 2):
            result.append(str(pre + 1) + "->" + str(i - 1))
        pre = i
    return result
