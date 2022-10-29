# https://leetcode.com/discuss/interview-question/1007960/Bloomberg-or-Phone-or-Find-all-ranges-of-consecutive-numbers-from-Array

# https://leetcode.com/problems/summary-ranges/

def summaryRanges(nums):

    if not nums:
        return []

    res = []
    nums = nums + [nums[-1]+2]  # adding a dummy number
    head = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            if head == nums[i-1]:
                res.append(str(head))
            else:
                res.append(str(head) + "->" + str(nums[i-1]))

            head = nums[i]
    return res
