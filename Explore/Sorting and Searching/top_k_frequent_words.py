from collections import defaultdict
from heapq import heappush, heappop, heappushpop


class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    # overriding the less than operator
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, words, k):
        mapper = defaultdict(int)
        for word in words:
            mapper[word] += 1

        h = list()
        for word, freq in mapper.items():
            node = Node(word, freq)
            if len(h) == k:
                heappushpop(h, node)
            else:
                heappush(h, node)

        result = list()
        while h:
            result.append(heappop(h).word)
        return result[::-1]
