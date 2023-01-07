
def minPathSum(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    memo = [[-1 for j in range(cols)] for i in range(rows)]
    memo[0][0] = grid[0][0]
    
    def dfs(m,n):
        
        if m < 0 or n < 0:
            return float('inf')

        if memo[m][n] != -1:
            return memo[m][n]
        
        up = grid[m][n] + dfs(m-1,n)
        left = grid[m][n] + dfs(m,n-1)
        
        memo[m][n] = min(up,left)
        
        return memo[m][n]
        
    return dfs(rows-1,cols-1)
        
