
# Time Complexity: O(n * 2^n), where n is the number of characters. In a worst case scenario
# Space Complexity: O(n * 2^n)
# There seems to be some disagreement online about the complexity of this problem; consider the following example to see the worst case scenario:

# s = aaaaaa
# wordDict = [a, aa, aaa, aaaa, aaaaa, aaaaaa]

# Our memo would look something like:
# {
#     "a": ["a"] ----------------------------------------- 2^0 items,
#     "aa": ["a a","aa"] ------------------------------ 2^1 items,
#     "aaa": ["a a a", "aa a", "a aa", "aaa"] - 2^2 items,
#     ...
# }
# That explains the space.

# The time could be explained by the number of executions of the subproblems.
# Namely, in the worst case we'd have to make n calls of the helper function,
# and each one of those calls would have 2^n append calls made, leaving us with O(n * 2^n)
def wordBreak(self, s, wordDict):
    wordSet = set(wordDict)
    memo = {}

    def helper(sub):
        if sub in memo:
            return memo[sub]
        result = []
        for i in range(len(sub)):
            prefix = sub[:i+1]
            if prefix in wordSet:
                if prefix == sub:
                    result.append(prefix)
                else:
                    restOfWords = helper(sub[i+1:])
                    for phrase in restOfWords:
                        result.append(prefix + " " + phrase)

        memo[sub] = result
        return result

    return helper(s)
