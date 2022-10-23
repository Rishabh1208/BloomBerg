# https://leetcode.com/discuss/interview-question/1007960/Bloomberg-or-Phone-or-Find-all-ranges-of-consecutive-numbers-from-Array

# Given a sorted array arr[] consisting of N integers without any duplicates, the task is to find the ranges of consecutive numbers from that array.

# Examples:
# Input: arr[] = {1, 2, 3, 6, 7}
# Output: 1->3, 6->7
# Explanation:
# There are two ranges of consecutive number from that array.
# Range 1 = 1 -> 3
# Range 2 = 6 -> 7
# Input: arr[] = {-1, 0, 1, 2, 5, 6, 8}
# Output: -1->2, 5->6, 8

# Explanation:
# There are three ranges of consecutive number from that array.
# Range 1 = -1 -> 2
# Range 2 = 5 -> 6
# Range 3 = 8

# https://leetcode.com/problems/summary-ranges/

def ranges(arr):
    ele = arr[0]
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 1:
            continue
        else:
            if ele != arr[i-1]:
                r = str(ele) + "-->" + str(arr[i-1])
                result.append(r)
            ele = arr[i]
    if ele != arr[i]:
        r = str(ele) + "-->" + str(arr[i])
        result.append(r)
    else:
        result.append(ele)
    return result


arr = [-1, 0, 1, 2, 5, 6, 8]
print(ranges(arr))
