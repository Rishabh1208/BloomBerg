
# Time compelxity: o(n2)
def maxContiguousSubarraySum(nums):
    n = len(nums)
    # Arbitrary minimum value for python
    max_sum = float('-inf')

    # Left will be the starting index of subarray
    for left in range(0, n):
        running_sum = 0
        # Right will be the ending index of subarray
        for right in range(left, n):

            # Add the current element to previous computed value
            # To get the subarray sum
            running_sum += nums[right]

            # Does this window beat the best sum we have seen so far?
            max_sum = max(max_sum, running_sum)

    return max_sum

# Time complexity: O(n)
def maxSubArray(nums):
    newNum = maxTotal = nums[0]

    for i in range(1, len(nums)):
        newNum = max(nums[i], nums[i] + newNum)
        maxTotal = max(newNum, maxTotal)

    return maxTotal
