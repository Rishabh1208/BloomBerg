# For word break, see the solution vidoe of the Leetcode solution.
# You should know the brute force soltuion with recursion
# how we can optimize it using cache ( recursion with memoization)
# lastly with DP. ( iterative solution)
# n is the length of the input string.
# Time complexity : O(n3). There are two nested loops, and substring computation at each iteration. 
# Overall that results in O(n3)O(n^3)O(n3) time complexity.
# Space complexity : O(n).

# def wordBreak(s, wordDict):
#     dp = [False] * (len(s)+1)

#     print(dp)
#     dp[len(s)] = True

#     for i in range(len(s)-1, -1, -1):
#         for w in wordDict:
#             if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
#                 dp[i] = dp[i+len(w)]
#             if dp[i]:
#                 break
#     return dp[0]


# s = "leetcode"
# wordDict = ["leet", "code"]
# print(wordBreak(s, wordDict))

# ............................................................................\
# DP with Trie

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


s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))
