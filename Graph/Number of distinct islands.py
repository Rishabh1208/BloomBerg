
def numDistinctIslands(grid):
    # Do a DFS to find all cells in the current island.
    def dfs(r, c, direction):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in seen or not grid[r][c]:
            return

        seen.add((r, c))
        path_signature.append(direction)

        dfs(r + 1, c, "D")
        dfs(r - 1, c, "U")
        dfs(r, c + 1, "R")
        dfs(r, c - 1, "L")
        # why we appending ("0") at the last. ( see the leetcode solution 3)
        path_signature.append("0")

    # Repeatedly start DFS's as long as there are islands remaining.
    seen = set()
    unique_islands = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            path_signature = []
            dfs(row, col, "0")
            if path_signature:
                unique_islands.add(tuple(path_signature))

    return len(unique_islands)


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]

print(numDistinctIslands(grid))
