from collections import defaultdict


def findLadders(beginWord, endWord, wordList):
    # to check if a word is existed in the wordSet, in O(1)
    wordSet = set(wordList)
    # wordSet.discard(beginWord)

    def neighbors(word):
        # change every possible single letters and check if it's in wordSet
        result = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i + 1:]
                if newWord in wordSet:
                    result.append(newWord)
        return result

    level = {}
    # level[word] is all possible sequence paths which start from beginWord and end at `word`.
    level[beginWord] = [[beginWord]]
    while level:
        nextLevel = defaultdict(list)
        for word, paths in level.items():
            if word == endWord:
                return paths  # return all shortest sequence paths
            for nei in neighbors(word):
                for path in paths:
                    # form new paths with `nei` word at the end
                    nextLevel[nei].append(path + [nei])
        # remove visited words to prevent loops
        wordSet -= set(nextLevel.keys())
        level = nextLevel  # move to new level

    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(findLadders(beginWord, endWord, wordList))
