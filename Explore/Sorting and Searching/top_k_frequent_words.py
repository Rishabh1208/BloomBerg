from collections import Counter
from heapq import heappush, heappop


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    # overiding the less than operator

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


def topKFrequent(words, k):
    cnt = Counter(words)
    h = []
    for word, freq in cnt.items():
        heappush(h, Pair(word, freq))
        if len(h) > k:
            heappop(h)
    print(h)
    return [p.word for p in sorted(h, reverse=True)]

words = ["i","love","leetcode","i","love","coding"]
k = 2

print(topKFrequent(words,k))