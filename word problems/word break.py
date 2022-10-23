
# Recursion with memoization TC: O(n3) n2 --> size of the recurison tree, n --> for checking every char (substring
# comparison)
# Example of s = 'leet' wordDict = ['l','e','ee','le','lee']
def wordBreak(self, s, wordDict):
    wordDict = set(wordDict)

    memo = {}

    def dfs(i):

        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        for j in range(i+1, len(s)+1):
            if s[i:j] in wordDict and dfs(j):
                memo[i] = True
                return memo[i]

        memo[i] = False
        return memo[i]

    return dfs(0)

# DP same Time complexity as before

def wordBreak(s, wordDict):

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if i+len(w) <= len(s) and s[i: i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]
