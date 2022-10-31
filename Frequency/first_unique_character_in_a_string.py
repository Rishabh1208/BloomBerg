
def firstUniqChar(s):
    freq = {}
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1

    for j in range(len(s)):
        if freq[s[j]] == 1:
            return j
    return -1

# TC: O(N), SC: O(1) space is O(1) because only 26 characters.
def firstUniqChar(s):
    arr = [0] * 26

    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1

    for i in range(len(s)):
        if arr[ord(s[i]) - ord('a')] == 1:
            return i

    return -1
