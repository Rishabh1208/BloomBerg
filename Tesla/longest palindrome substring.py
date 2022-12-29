def longestPalindrome(self, s):
    # Helper function to check
    def helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    res = ''
    for i in range(len(s)):
        # odd string
        temp = helper(s, i, i)
        if len(temp) > len(res):
            res = temp

        # even string
        temp = helper(s, i, i+1)
        if len(temp) > len(res):
            res = temp

    return res
