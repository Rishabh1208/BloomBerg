def uniqueOccurrences(self, arr):
    freq = {}
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    unique = set(freq.values())

    return len(freq) == len(unique)
