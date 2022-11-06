def getSmallestString(self, n, k):
    res = ["a"] * n
    k -= n
    cur = n-1
    while k > 0:
        res[cur] = chr(ord("a") + min(k, 25))
        cur -= 1
        k -= 25
    return "".join(res)
