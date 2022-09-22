import collections


def minSteps(s, t):
    memo = collections.defaultdict(int)
   # saving the number of occurance of characters in s
    for char in s:
        memo[char] += 1

    count = 0
    for char in t:
        if memo[char]:
            # if char in t is also in memo, substract that from the counted number
            memo[char] -= 1
        else:
            count += 1
    # return count #or
    return sum(memo.values())


def minSteps(s, t):
    count = collections.Counter(s)
    res = 0

    for c in t:
        if count[c] > 0:
            count[c] -= 1
        else:
            res += 1

    return res


s = "leetcode"
t = "practice"

print(minSteps(s, t))
