
# intuition:

# initialize a matrix of zeros
# fill in the numbers in a spiral order layer-by-layer
def generateMatrix(self, n):
    if not n:
        return []
    matrix = [[0] * n for _ in range(n)]
    
    # layer by layer strategy
    num = 1
    top = 0  # top layer: top row index
    right = n - 1  # right layer: right col index
    down = n - 1  # bottom layer: bottom row index
    left = 0  # left layer: left col index

    # while layers closing inward but not overlapping. 
    # if overlap = reached end of spiral matrix
    while left <= right and top <= down:
        # top row
        # from left to right. right + 1 to reach the last position in a row
        for i in range(left, right+1):
            # to fill top row, fix the top row index and increment the col position
            matrix[top][i] = num
            num += 1  # update num
        # after traversing top row, move top row index inward(downward) by one unit
        top += 1

        # right col
        # from top to bottom. bottom + 1 to reach the last positin in a col
        for i in range(top, down+1):
            # to fill the right col, fix the right col index and increment the row position
            matrix[i][right] = num
            num += 1  # update num
        # after traversing right col, move right col index inward(towards the left) by one unit
        right -= 1

        # bottom row
        # from left to right, in reverse order. left-1 to reach the leftmost position in a row
        for i in range(right, left-1, -1):
            matrix[down][i] = num
            num += 1  # update num
        # after traversing bottom row, move bottom row index inward(upward) by one unit
        down -= 1

        # left col
        # from bottom to top, in reverse order. top-1 to reach the topmost position in a col
        for i in range(down, top-1, -1):
            # to fill the left col, fix the left col index and increment the row position
            matrix[i][left] = num
            num += 1
        # after traversing left col, move left col index inward(towards the right) by one unit
        left += 1

        # repeat until top-bottom or left-right indices collide (ie. have completed all layers)
    return matrix
