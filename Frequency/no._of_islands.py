def numIslands(self, grid):
    rows = len(grid)
    cols = len(grid[0])

    if not grid:
        return 0

    count = 0

    # visited grid
    visited = [[False for c in range(cols)] for r in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or visited[r][c]:
            return

        visited[r][c] = True

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                dfs(r, c)
                count += 1
    return count
