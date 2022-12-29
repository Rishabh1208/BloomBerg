# Recursion with memoization
def frogJump(n,heights):
    dp = [-1 for i in range(n)]
    def helper(idx):
        if idx == 0:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        firstStep = helper(idx-1) + abs(heights[idx] - heights[idx-1])
        secondStep = float('inf')
        if idx > 1:
            secondStep = helper(idx-2) + abs(heights[idx] - heights[idx-2])
            
        dp[idx]= min(firstStep, secondStep)
        return dp[idx]
        
        
    return helper(n-1)

# Tabulation
def frogJump(n,heights):
    dp = [-1 for i in range(n)]
    dp[0] = 0
    for idx in range(1,n):
        firstStep = dp[idx-1] + abs(heights[idx] - heights[idx-1])
        secondStep = float('inf')
        if idx > 1:
            secondStep = dp[idx-2] + abs(heights[idx] - heights[idx-2])
        dp[idx] = min(firstStep, secondStep)
        
    return dp[n-1]

n = 4
heights = [10,20,30,10]
print(frogJump(n,heights))
        
       
        
        
    
