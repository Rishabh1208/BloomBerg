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
        