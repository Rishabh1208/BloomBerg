# Given a collection of intervals, return a maximal set of non-overlapping intervals
# while prioritising the longer intervals.

# input - (1,5),(2,7),(11,18)
# output - (11, 18), (2, 7)


def chooseIntervals(intervals):
    intervals.sort(key=lambda x: x[0])

    res = []

    for interval in intervals:
        if len(res) == 0 or interval[0] >= res[-1][1]:
            res.append(interval)
        elif interval[1] - interval[0] > res[-1][1] - res[-1][0]:
            res[-1] = interval

    return res


intervals = [[1, 5], [2, 7], [6, 10]]
print(chooseIntervals(intervals))
