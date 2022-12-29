
import heapq


def minMeetingRooms(intervals):
    intervals.sort()
    rooms = []
    heapq.heappush(rooms, intervals[0][1])

    for start, end in intervals[1:]:
        if start < rooms[0]:
            heapq.heappush(rooms, end)
        else:
            heapq.heappushpop(rooms, end)

    return len(rooms)


# .....................................................................................

# choronlogical sorting.(greedy approach)
def minMeetingRooms(intervals):
    startTime = sorted([x for x, y in intervals])
    endTime = sorted([y for x, y in intervals])
    count = 0
    i = 0  # startTime
    j = 0  # EndTime

    while i < len(startTime):
        if startTime[i] < endTime[j]:
            count += 1
            i += 1
        # It covers equals case as well. ( why we are not decrementing count, take an example, 
        # where startTime -> 12 and endTime -> 11
        # that means one room is gonna get free but at the same time we are allocating 
        # one more room that gonna nullify the count)
        else:
            i += 1
            j += 1

    return count
