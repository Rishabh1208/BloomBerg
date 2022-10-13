# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# time complexity: o(n* 2^n) because at every step we have two choices either to include
# an element or not include an element.
# space complexity: o(N)

# simple backtracking on whther to include an element or not include an element.
def subsets(self, nums):
    res = []
    subset = []
    
    def dfs(i):
        if i >= len(nums):
            res.append(subset)
            return
        
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)
        
        # decision Not to include nums[i]
        subset.pop()
        dfs(i+1)
        
    dfs(0)
    return res

