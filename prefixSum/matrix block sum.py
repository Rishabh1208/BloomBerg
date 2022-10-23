def matrixBlockSum(mat, K):
    rows = len(mat)
    cols = len(mat[0])

    matrix = [[0 for c in range(cols+1)] for r in range(rows+1)]
    # adding one row and one column above and left of it so that it can handle boundary conditions.
    for r in range(rows):
        prefix = 0
        for c in range(cols):
            prefix += mat[r][c]
            above = matrix[r][c+1]
            matrix[r+1][c+1] = prefix + above
    print(matrix)

    # Compute Block Sum
    for i in range(rows):
        min_r, max_r = max(0, i - K), min(rows, i + K+1)
        for j in range(cols):
            min_c, max_c = max(0, j - K), min(cols, j + K+1)
            mat[i][j] = matrix[max_r][max_c] - matrix[min_r][max_c] - matrix[max_r][min_c] + matrix[min_r][min_c]

    return mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
print(matrixBlockSum(mat, k))
