# https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number

# this leads to infinite loop try 11
# def generateSteps(target):
#     steps = 0

#     def dfs(n, c):
#         nonlocal steps

#         if n == target:
#             return steps

#         steps += 1

#         if n < target:
#             dfs(n*2, c+1)

#         else:
#             dfs(n//3, c+1)

#     dfs(1, 0)
#     return steps


# target = 11
# print(generateSteps(target))


from collections import deque


def minNumber2(n):
    q = deque([(1, 0)])
    seen = set()

    while q:
        res, ops = q.popleft()

        if res == n:
            return ops
        if res//3 not in seen:
            q.append((res//3, ops+1))
            seen.add(res//3)

        if res*2 not in seen:
            q.append((res*2, ops+1))
            seen.add(res*2)


print(minNumber2(10))
print(minNumber2(3))
print(minNumber2(11))


# Input: 10
# Output: 6
# Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
# 6 steps required, as we have used 5 multiplications by 2, and one division by 3.
