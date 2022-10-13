def longestPalindrome(s):
    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(s, l, r):
        print(s, l, r)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        print(s[l+1:r])
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        
        tmp = helper(s, i, i)
        res = max(tmp, res)

        # even case, like "abba"
        tmp = helper(s, i, i+1)
        res = max(tmp, res)

    
    return res


s = "babad"
longestPalindrome(s)
