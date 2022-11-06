def sortedSquares(self, nums):
    result = [None] * len(nums)
    left = 0
    right = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left]**2
            left += 1
        else:
            result[i] = nums[right]**2
            right -= 1
    return result

# Approach1 : simple square it and sort it.
# Approach2: Two pointer approach (Good question) t(n) - O(n), S(n) - O(n)
