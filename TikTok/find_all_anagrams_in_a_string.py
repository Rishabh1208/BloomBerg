# s = "cbaebabacd", p = "abc"
def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    c1 = {}
    c2 = {}
    for i in range(len(p)):
        c1[p[i]] = c1.get(p[i], 0) + 1
        c2[s[i]] = c2.get(s[i], 0) + 1

    res = []
    left = 0
    if c1 == c2:
        res.append(0)

    for r in range(len(p), len(s)):
        c2[s[r]] = c2.get(s[r], 0) + 1
        c2[s[left]] -= 1
        if c2[s[left]] == 0:
            del c2[s[left]]
        left += 1
        if c1 == c2:
            res.append(left)
    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
