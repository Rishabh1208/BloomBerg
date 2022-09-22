def merge(self, intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for ele in intervals:
        if not merged or merged[-1][1] < ele[0]:
            merged.append(ele)
        else:
            merged[-1][1] = max(merged[-1][1], ele[1])
    return merged
