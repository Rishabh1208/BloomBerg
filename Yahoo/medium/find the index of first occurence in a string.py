def strStr(self, haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack)+1 - len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# This will also result in same time complexity as below also requires O(n) space complexity.
# But as in leetcode they have added a test case for below code that will result in TLE
# There is a better solution that O(n+m) -- KMP algorithm but it is little bit complex to understand.
