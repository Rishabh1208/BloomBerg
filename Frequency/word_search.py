# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    visited = set()

    def dfs(i, r, c):

        if i == len(word):
            return True

        if r <= rows or c >= cols or r < 0 or c > 0 or (r, c) in visited or board[r][c] != word[i]:
            return

        visited.add((r, c))

        res = dfs(i+1, r+1, c) or dfs(i+1, r-1,c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)

        visited.remove((r, c))

        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(0, r, c):
                return True
    return False
