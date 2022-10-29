from collections import deque


class Solution(object):
    import collections
    from collections import deque

    def ladderLength(self, beginWord, endWord, wordList):
        # Time ccomplexity: O(M*M *N) N --> no. of words in wordList and m --> char in a word
        # space complexity: O(M*N)
        # Better approach: Take a set of wordlist and then also for every word in wordlist, try every combination from a-z for every char in word.
        q = deque([beginWord])
        visited = set([beginWord])
        wordSet = set(wordList)

        changes = 1
        alph = "abcdefghijklmnopqrstuvwxyz"

        if endWord not in wordList:
            return 0

        while q:
            for i in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return changes

                for i in range(len(curr_word)):
                    prefix, suffix = curr_word[:i], curr_word[i+1:]
                    for ch in alph:
                        w = prefix + ch + suffix
                        if w in wordSet and w not in visited:
                            q.append(w)
                            visited.add(w)
            changes += 1
        return 0


#         # This is the graph problem.
#         # To Find the shortest path in a graph. Always use BFS.
#         # For n nodes(vertices), maximum you could have is n^2 edges.
#         if endWord not in wordList:
#             return 0

#         nei = collections.defaultdict(list)
#         wordList.append(beginWord)
#         # Making adjacency list. For eg - hot --> *ot, h*t, ho*
#         for word in wordList:
#             for j in range(len(word)):
#                 pattern = word[:j] + "*" + word[j + 1 :]
#                 nei[pattern].append(word)

#         visit = set([beginWord])
#         q = deque([beginWord])
#         res = 1
#         while q:
#             for i in range(len(q)):
#                 word = q.popleft()
#                 if word == endWord:
#                     return res
#                 for j in range(len(word)):
#                     pattern = word[:j] + "*" + word[j + 1 :]
#                     for neiWord in nei[pattern]:
#                         if neiWord not in visit:
#                             visit.add(neiWord)
#                             q.append(neiWord)
#             res += 1
#         return 0
