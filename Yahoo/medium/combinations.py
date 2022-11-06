
def combinations(n, k):
    result = []

    def backtrack(start, comb):
        if len(comb) == k:
            result.append(comb[:])
            return

        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
    backtrack(0, [])
    return result
