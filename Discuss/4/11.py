

# https://leetcode.com/discuss/interview-question/1608777/Bloomberg-or-Phone-Screen-or-Find-Path-bw-2-objects-in-a-desert

# Interviewer asked about background for 10 mins. Then moved to ask question:

# Given a 2d matrix that represents a matrix where . denotes empty land, c indicates car,
# and o indicates oasis, and another integer gas which indicates gas we have left.
# Traversing one unit in the matrix consumes 1 gas unit. You can move up, down, left, and right.
# So Example: the matrix below and gas = 5 returns true since we can get from c to o in 5 units
# (1 unit left, 3 units down, and 1 unit right)
# [[. . . c .]
# [. . . . .]
# [. . . . .]
# [ . . o . .]]

# a) Check if car can reach oasis or not. (return bool val)
# b) Now suppose there is a gas station in the matrix somewhere that is denoted by an integer
# k where k represents the gas units that the car will be refuelled. So if k is 2, car will gain gas.
# Check if car can still reach oasis (with or without gas station).

# ^This was the part that confused me.

# c) Now let's say there's obstacles in the matrix represented by r. how would you check if
# car can reach oasis? (Answered dfs with memoization)

# Would really appreciate if someone can share their approach to this problem! (preferrably in Python)


from collections import deque


def matrix(arr, gas, k):
    rows = len(arr)
    cols = len(arr[0])
    visited = set()

    def bfs(i, j):
        q = deque()
        q.append([i, j])
        steps = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                if steps > gas:
                    return False
                if arr[x][y] == 'o' and steps <= gas:
                    print("steps", steps)
                    return True

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for r, c in directions:
                    rx = x+r
                    cy = y+c
                    if rx in range(rows) and cy in range(cols) and (rx, cy) not in visited and arr[rx][cy] != 'r':
                        if arr[rx][cy] == 'k':
                            gas += k
                        q.append([rx, cy])
                        visited.add((rx, cy))
            steps += 1
        return False

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == "c":
                return bfs(i, j)


arr = [[".", ".", ".", "c", "."],
       [".", ".", ".", ".", "."],
       [".", ".", ".", ".", "."],
       [".", ".", "o", ".", "."]]

gas = 5
k = 2
print(matrix(arr, gas, k))
