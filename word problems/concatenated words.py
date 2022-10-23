def findAllConcatenatedWordsInADict(words):
    words = set(words)
    memo = {}

    def dfs(word):
        if word in memo:
            return memo[word]
        for second_idx in range(1, len(word)):
            prefix, suffix = word[:second_idx], word[second_idx:]
            if prefix in words and suffix in words or prefix in words and dfs(suffix):
                memo[word] = True
                return True
        memo[word] = False
        return False

    result = []
    for word in words:
        if dfs(word):
            result.append(word)
    return result


words = ["cat", "cats", "catsdogcats", "dog",
         "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

print(findAllConcatenatedWordsInADict(words))

# .............................................................................

# reusing of workbreak 1 solution
def findAllConcatenatedWordsInADict(words):

    wordDict = []
    words.sort(key=lambda x: len(x))

    def dfs(word):  # word break 1 dp solution
        dp = [False] * (len(word) + 1)
        dp[len(word)] = True

        for i in range(len(word)-1, -1, -1):
            for w in wordDict:
                if i+len(w) <= len(word) and word[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]

    result = []
    for word in words:
        if dfs(word):
            result.append(word)

        wordDict.append(word)
    return result
