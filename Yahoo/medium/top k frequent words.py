from collections import Counter
from collections import defaultdict
from heapq import heappush, heappop, heapify

# HELPER CLASS


class Item(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    # override the comparison operator - heapq internally uses this for comparison
    def __lt__(self, other):
        if self.freq == other.freq:
            # this step is important!
            # since we need word with lower aplha order first in FINAL RESULT
            # and this Final result will be achieved by reversing the temp result array
            # SO HERE, we return self.word>other.word instead of self.word<other.word
            # Think :)
            return self.word > other.word

        return self.freq < other.freq

# MAIN CLASS


class Solution:
    def topKFrequent(self, words, k):
        mapper = defaultdict(int)
        for word in words:
            mapper[word] += 1

        h = list()
        for word, freq in mapper.items():
            node = Item(word, freq)
            heappush(h, node)

            if len(h) > k:
                heappop(h)

        result = list()
        while h:
            result.append(heappop(h).word)
        return result[::-1]

# bucket sort for frequency and if same frequency then Trie for traversing lexographically.


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        cnt = Counter(words)
        bucket = [{} for _ in range(n+1)]
        self.k = k

        def add_word(trie: Mapping, word: str) -> None:
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]
            root['#'] = {}

        def get_words(trie: Mapping, prefix: str) -> List[str]:
            if self.k == 0:
                return []
            res = []
            if '#' in trie:
                self.k -= 1
                res.append(prefix)
            for i in range(26):
                c = chr(ord('a') + i)
                if c in trie:
                    res += get_words(trie[c], prefix+c)
            return res

        for word, freq in cnt.items():
            add_word(bucket[freq], word)

        res = []
        for i in range(n, 0, -1):
            if self.k == 0:
                return res
            if bucket[i]:
                res += get_words(bucket[i], '')
        return res
