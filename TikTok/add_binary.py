def addBinary(self, a, b):
    n = max(len(a), len(b))
    # zfill - fill zeroes at the initial.
    a = a.zfill(n)
    b = b.zfill(n)
    # carry is needed.
    carry = 0
    res = []
    for i in range(n-1, -1, -1):
        if a[i] == "1":
            carry += 1
        if b[i] == "1":
            carry += 1

        if carry % 2 == 0:
            res.append("0")
        else:
            res.append("1")
        carry = carry//2
    if carry == 1:
        res.append("1")
    res.reverse()
    return "".join(res)
