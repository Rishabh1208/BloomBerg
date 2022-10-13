import heapq

# heap O(NlogN)
def minMeetingRooms(intervals):
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0
    # The heap initialization
    free_rooms = []
    # Sort the meetings in increasing order of their start time.
    intervals.sort(key=lambda x: x[0])
    # Add the first meeting. We have to give a new room to the first meeting.
    heapq.heappush(free_rooms, intervals[0][1])
    # For all the remaining meeting rooms
    for i in intervals[1:]:
        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)
        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])
    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)

# ...............................................................................
# chronological ordering
# O(N)
def minMeetingRooms(self, intervals):
    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    count, res = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(count, res)
    return res
