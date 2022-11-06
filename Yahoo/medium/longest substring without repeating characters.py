def lengthOfLongestSubstring(self, s):

    # sliding window technique
    chars = {}
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


def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    ans = 0
    mp = {}

    i = 0
    for j in range(n):
        if s[j] in mp:
            # why we are using i try this example: a,b,b,a
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans
