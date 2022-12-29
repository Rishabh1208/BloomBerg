
def minOperations(s):

    n = len(s)
    res1 = res2 = 0

    for i in range(n):
        if int(s[i]) == i % 2:
            res1 += 1
        else:
            res2 += 1

    return min(res1, res2)
