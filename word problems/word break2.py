
# Example s = 'catsanddoggo' , wordDict = ['cat','cats','and','sand','dog','do','go]
# TC: 2^N + N^2 + W , SC: O(2N⋅N+W)

def wordBreak(s, wordDict):
    wordDict = set(wordDict)
    memo = {}

    def dfs(string):
        if string in memo:
            return memo[string]

        result = []
        for i in range(len(string)):
            prefix = string[:i+1]
            if prefix in wordDict:
                if prefix == string:  # if we reached at the end of the string.
                    result.append(prefix)
                else:
                    # if we haven't reached at the end of string.
                    restWords = dfs(string[i+1:])
                    for word in restWords:
                        result.append(prefix + " " + word)
        memo[string] = result
        return memo[string]

    return dfs(s)


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, wordDict))
