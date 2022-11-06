def characterReplacement(self, s, k):
    left = 0
    freq = {}
    longest_str = 0
    window = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        window = right - left + 1
        if window - max(freq.values()) <= k:
            longest_str = max(longest_str, window)
        else:
            freq[s[left]] -= 1
            left += 1
    return longest_str
