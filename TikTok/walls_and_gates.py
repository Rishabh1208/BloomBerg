from collections import deque

# brute force approach would be to visit every cell and see which could be closest
# cell but time complexity would be O(m*n)2. DFS solution

# Better approach: BFS solution, intution, instead of starting from rooms.
# Simultaneously do the Bfs from all the gates othwerwise it would result wrong ans.
# Time complexity: O(m*n)
# space complexity: o(m*n)

# BFS solution
def wallsAndGates(rooms):
    rows, cols = len(rooms), len(rooms[0])
    visit = set()
    #queue
    q = deque()

    def addRooms(r, c):
        if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or rooms[r][c] == -1:
            return
        visit.add((r, c))
        q.append([r, c])

    for r in range(rows):
        for c in range(cols):
            # checking if it is gate or not
            if rooms[r][c] == 0:
                visit.add((r, c))
                q.append([r, c])

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = dist
            addRooms(r+1, c)
            addRooms(r-1, c)
            addRooms(r, c+1)
            addRooms(r, c-1)
        dist += 1
