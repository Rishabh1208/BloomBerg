# https://leetcode.com/discuss/interview-question/1247447/Bloomberg-Onsite-SDE-Reject


# Given some numbers [3,5,7,8,10], and interval list : [1,6,15] , they wanted to know
# how many numbers occur between each interval .
# The answer for this example will be : [2,3] i.e [1,6] -> [3,5] and [6,15] -> [7,8,10].
# I clarified the interval assumptions. the boundaries inclusivity & exclusivity.
# I gave a binary search related answer, after sorting out the numbers.
# Collaborated perfectly during the entire time.
# The Solution I coded out :
# For each element in intervals list , using Binary search get the index of
# element just less than or equal to the given element
# eg for intervals [1,6,15] : [-1,1,4]
# return the difference array : [(1-(-1)),(4-1)] : [2,3]

def solve(nums, ranges):

    mp = dict()

    for num in nums:
        mp[num] = 1

    result = []

    for x in range(1, len(ranges)):

        count = 0
        minVal = ranges[x-1]
        maxVal = ranges[x]

        for x in range(minVal, maxVal):
            if x in mp:
                count += 1

        result.append(count)

    return result


def numbersInIntervals(nums, intervals):
    i = 0
    start, end = 0, 1
    res = []
    while i < len(nums) and end < len(intervals):
        count = 0
        while i < len(nums) and nums[i] < intervals[start]:
            i += 1
        while i < len(nums) and nums[i] < intervals[end]:
            count += 1
            i += 1

        start += 1
        end += 1

        res.append(count)

    return res
