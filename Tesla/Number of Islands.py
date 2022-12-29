from collections import deque


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

# without visited set(), manipulating the matrix itself.
# TC: O(mn), SC: O(mn) [Recursion stack]


def numIslands(grid):
    def part_of_island(i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'

        part_of_island(i, j+1, grid)
        part_of_island(i, j-1, grid)
        part_of_island(i+1, j, grid)
        part_of_island(i-1, j, grid)

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands += 1
                part_of_island(i, j, grid)
    return islands

# BFS (it is better approach because space time complexity would be O(min(m,n)))
# https://imgur.com/gallery/M58OKvB [why O(min(m,n))]
# Time complexity would be O(mn)


def numberOfIslands(grid):

    if not grid:  # edge case
        return 0

    rows = len(grid)  # rows length
    cols = len(grid[0])  # column length

    def bfs(grid, queue):
        queue.append((r, c))
        grid[r][c] = "0"

        while queue:
            r, c = queue.popleft()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                rr = r + dr
                cc = c + dc
                if rr in range(rows) and cc in range(cols) and grid[rr][cc] == "1":
                    queue.append((rr, cc))
                    grid[rr][cc] = "0"

    count = 0
    queue = deque([])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                bfs(grid, queue)
                count += 1

    return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numberOfIslands(grid))
