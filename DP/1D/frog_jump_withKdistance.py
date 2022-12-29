# Recursion with memoization
def frogKJump(n,heights,k):
    dp = [-1 for i in range(n)]
    def helper(idx):
        if idx == 0:
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        minSteps = float('inf')
        for j in range(1,k+1):
            if j-k >=0:
                jump = helper(idx-1) + abs(heights[idx] - heights[idx-1])
                minSteps = min(minSteps, jump)
       
        dp[idx]= minSteps
        return dp[idx]
        
    return helper(n-1)

# Tabulation
def frogKJump(n,heights,k):
    dp = [-1 for i in range(n)]
    
    dp[0] = 0
    for idx in range(1,n):
        minSteps = float('inf')
        
        for j in range(1, k+1):
            if j-k >=0:
                jump = dp[idx-1] + abs(heights[idx] - heights[idx-1])
                minSteps = min(minSteps, jump)
                
        dp[idx] = minSteps
        
    return dp[n-1]

