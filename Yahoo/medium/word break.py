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
