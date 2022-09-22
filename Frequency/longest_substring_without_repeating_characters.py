def lengthOfLongestSubstring(self, s):

    # sliding window technique
    chars = {}
    longStr = {}

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[r] = chars.get(r, 0) + 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res
