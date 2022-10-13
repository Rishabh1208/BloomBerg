# group by characters (approach)

# Time complexity - O(n)
# space complexity - O(n)
def countBinarySubstrings(self, s):
    groups = [1]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            groups.append(1)
        else:
            groups[-1] += 1

    ans = 0
    for i in range(1, len(groups)):
        ans += min(groups[i-1], groups[i])
    return ans

# Time complexity - O(n)
# space complexity - O(1)
# s = "00110011"
def countBinarySubstrings(self, s):
    ans, prev, cur = 0, 0, 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            ans += min(prev, cur)
            prev, cur = cur, 1
        else:
            cur += 1

    return ans + min(prev, cur)
