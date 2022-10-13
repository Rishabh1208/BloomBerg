def islandPerimeter(grid):
    R, C = len(grid), len(grid[0])
    perimeter = 0
    # Traverse the grid
    for i in range(R):
        for j in range(C):
            # If it is a land block increment perimeter by 4
            if grid[i][j] == 1:
                perimeter += 4
        # Check whether top neighbour is a land and decrement it by 2
        # as it intersects
            if i > 0 and grid[i-1][j] == 1:
                perimeter -= 2
        # Check left neighbour is a land and decrement it by 2
        # as it intersects
            if j > 0 and grid[i][j-1] == 1:
                perimeter -= 2
    return perimeter


def islandPerimeter(grid):
    R, C = len(grid), len(grid[0])
    perimeter = 0
    # Traverse the grid
    for i in range(R):
        for j in range(C):
            # If it is a land block increment perimeter by 4
            if grid[i][j] == 1:
                perimeter += 4
                # Check each neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if i < R-1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < C-1 and grid[i][j+1] == 1:
                    perimeter -= 1
    return perimeter
