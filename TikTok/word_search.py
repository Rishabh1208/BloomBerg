# Time complexity: O(m*n) * dfs -- since we are calling dfs 4 times and max
# we could go to lenght of word, therefore overall O(m*n) * 4^len(word)
# space complexity: len(word)

# Normal backtracking.
def exist(self, board, word):
    rows = len(board)
    cols = len(board[0])
    path = set()

    def dfs(r, c, i):
        # base condition
        if i == len(word):
            return True

        if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in path or word[i] != board[r][c]):
            return False
        
        # adding to the visited path
        path.add((r, c))
        
        # Exploring all the paths, any paths could lead us to the answer that's why using
        # or. and if exploring all the paths of that current node, we would backtrack
        # by removing all the nodes we visited while exploring.
        res = (dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1) or
               dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1))

        # removing from the visited path
        path.remove((r, c))

        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
