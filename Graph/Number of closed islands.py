def closedIsland(self, grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    visited = set()  # instead of taking visit set you can just manipulate the board to be -1 whenever you find any 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False

        if (r, c) in visited or grid[r][c] == 1:
            return True

        visited.add((r, c))
        # This is interesting case if you do return dfs(r-1,c) and dfs(r+1,c) and dfs(r,c+1) and dfs(r,c-1) , This will won't work. why > see this discussion and comment
        # https://leetcode.com/problems/number-of-closed-islands/discuss/1250335/DFS-oror-Well-explained-oror-93-faster-oror
        up = dfs(r-1, c)
        down = dfs(r+1, c)
        right = dfs(r, c+1)
        left = dfs(r, c-1)
        return up and down and right and left

    # reason why we are not checking border cells because we know if 0 would be there in those
    # border we couldn't find the soltuon because it has to be closed island
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if grid[r][c] == 0 and (r, c) not in visited and dfs(r, c):
                count += 1

    return count
