class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isWordEnd = True

    def search(self, s):
        curr = self.root
        for ele in s:
            if ele not in curr.children:
                return False
            curr = curr.children[ele]
        return curr.isWordEnd

# using Trie
def wordBreak(s, wordDict):
    trie = Trie()
    for dict in wordDict:
        trie.add(dict)

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and trie.search(s[j:i]):
                dp[i] = True
                break
    return dp[-1]

# If you wanna normal recursion, just remove the memo part from this basic memoization function.
# memoization
def wordBreak(self, s, wordDict):
    # memo = {}

    def wordBreakMemo(s, word_dict, start):
        if start == len(s):
            return True
        # if start in memo:
        #     return memo[start]
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                # memo[start] = True
                return True

        # memo[start] = False
        return False

    return wordBreakMemo(s, set(wordDict), 0)

# using DP
def wordBreak(self, s, wordDict):
    dp = [False] * (len(s)+1)

    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]
