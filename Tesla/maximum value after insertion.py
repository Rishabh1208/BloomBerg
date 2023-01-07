def maxValue(n, x):
    if n[0] == '-':
        idx = 1
        while idx < len(n) and x >= int(n[idx]):
            idx += 1
    else:
        idx = 0
        while idx < len(n) and x <= int(n[idx]):
            idx += 1
    ans = n[:idx] + str(x) + n[idx:]
    return ans


n = "99"
x = 9