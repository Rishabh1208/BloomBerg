# A labyrinth of zeros and ones is given. Zero - "cannot pass", One - "can pass."
# List all paths from top left to bottom-right corner. You can move only down or to the right.
# Input: 2-dimensional array that contains the labyrinth.
# Example:
# Input = [[1,0,1], [1,1,1], [0,1,1]]
# Input in 2D:
# 1 0 1
# 1 1 1
# 0 1 1

# Output:
# (0,0) (1,0) (1,1) (2,1) (2,2)
# (0,0) (1,0) (1,1) (1,2) (2,2)

# if impossible to reach bottom-right corner, print "No paths."

def PathToTarget(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = []

    def dfs(path, x, y):
        if x >= rows or y >= cols or grid[x][y] == 0:
            return

        path.append((x, y))

        if x >= rows-1 and y >= cols-1:
            result.append(path[:])
            return

        dfs(path, x+1, y)  # down
        dfs(path, x, y+1)  # right

    dfs([], 0, 0)
    return result if len(result) > 0 else "No Paths"


grid = [[1, 0, 1], [1, 1, 1], [0, 1, 1]]
print(PathToTarget(grid))
