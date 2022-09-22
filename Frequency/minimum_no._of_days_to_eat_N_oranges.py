

from collections import deque


# def minDays(n):
#     dp = {0: 0, 1: 1}

#     def dfs(n):
#         if n in dp:
#             return dp[n]

#         one = 1 + (n % 2) + dfs(n//2)
#         two = 1 + (n % 3) + dfs(n//3)
#         dp[n] = min(one, two)
#         return dp[n]
#     return dfs(n)


def minDays(n):
    q = deque()
    q.append(n)
    steps = 0
    visited = set()

    while q:
        steps += 1
        for _ in range(len(q)):
            x = q.popleft()
            if x % 3 == 0 and x//3 not in visited:
                q.append(x//3)
                visited.add(x//3)
            if x % 2 == 0 and x//2 not in visited:
                visited.add(x//2)
                q.append(x//2)
            if x-1 not in visited:
                visited.add(x-1)
                q.append(x-1)
            if x-1 == 0 or x == 0:
                return steps


n = 10
print(minDays(n))
