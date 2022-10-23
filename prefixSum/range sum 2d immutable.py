class NumMatrix(object):

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.updatedMatrix = [
            [0 for c in range(cols+1)] for r in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.updatedMatrix[r][c+1]
                self.updatedMatrix[r+1][c+1] = prefix + above

    def sumRegion(self, row1, col1, row2, col2):
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.updatedMatrix[r2][c2]
        above = self.updatedMatrix[r1-1][c2]
        left = self.updatedMatrix[r2][c1-1]
        ele = self.updatedMatrix[r1-1][c1-1]
        return bottomRight - above - left + ele


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
