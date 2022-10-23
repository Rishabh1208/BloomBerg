def floodFill(image, sr, sc, newColor):
    r, c = len(image), len(image[0])
    color = image[sr][sc]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c:
            return
        if image[i][j] == newColor or image[i][j] != color:
            return
        image[i][j] = newColor
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    dfs(sr, sc)
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))
