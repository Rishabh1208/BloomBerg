def canVisitAllRooms(self, rooms):
    seen = [False] * len(rooms)
    seen[0] = True
    stack = [0]

    while stack:
        room = stack.pop()
        for nei in rooms[room]:
            if not seen[nei]:
                stack.append(nei)
                seen[nei] = True

    # The all() function returns True if all items in an iterable are true, otherwise it returns False.
    # If the iterable object is empty, the all() function also returns True.

    return all(seen)
