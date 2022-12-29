class Solution(object):
    def maxSubArray(self, nums):
        total = 0
        maxNum = -1000000
        for ele in nums:
            total += ele
            maxNum = max(total,maxNum)
            if total < 0:
                total = 0
        return maxNum
    
    
# Brute-force approach -:
#     Approach 1: Using 2 for loops
# Starting from index i, start adding the numbers and record the maximum sum with all the next elements.
# Doing this for every i element (n-i) times will cause time complexity to become O(n^2).

# Simpler approach :- BEST APPROACH
# def maxSubArray(self, nums: List[int]) -> int:        
# 	newNum = maxTotal = nums[0]        
	
# 	for i in range(1, len(nums)):
# 		newNum = max(nums[i], nums[i] + newNum)
# 		maxTotal = max(newNum, maxTotal)

# 	return maxTotal	


        