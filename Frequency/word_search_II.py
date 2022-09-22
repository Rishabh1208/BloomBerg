
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWOrd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isEndOfWOrd = True


def findWords(board, words):
    root = Trie()
    for w in words:
        root.add(w)

    rows = len(words)
    cols = len(words[0])

    visited = set()
    result = set()

    def dfs(node, r, c, path):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] not in node.children:
            return

        visited.add((r, c))
        node = node.children[board[r][c]]
        path += board[r][c]
        if node.isEndOfWord:
            result.add(path)

        dfs(node, r+1, c, path)
        dfs(node, r-1, c, path)
        dfs(node, r, c+1, path)
        dfs(node, r, c-1, path)

        visited.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(root, r, c, " ")

    return result
