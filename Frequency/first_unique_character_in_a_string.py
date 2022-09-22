def firstUniqChar(self, s):
    freq = {}
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1

    for j in range(len(s)):
        if freq[s[j]] == 1:
            return j
    return -1
