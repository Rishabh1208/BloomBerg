from collections import Counter
import heapq


def topKFrequent(nums, k):
    res = []
    mp = {}
    # This is Heap solution, Better solution should be bucket sort
    # somer imp. points to consider for heap
    # heapq.heapify o(n), heapq.heappush, heapq.heappushpop
    # T(n) - klogn, s(n) - k
    for i in range(len(nums)):
        mp[nums[i]] = mp.get(nums[i], 0) + 1

    for key, value in mp.items():
        if len(res) < k:
            heapq.heappush(res, [value, key])
        else:
            heapq.heappushpop(res, [value, key])

    return [key for value, key in res]


def topKFrequent(nums, k):
    freq = Counter(nums)
    arr = [[] for i in range(len(nums)+1)]
    res = []
    for key, value in freq.items():
        arr[value].append(key)
    for i in range(len(arr)-1, 0, -1):
        if arr[i]:
            for ele in arr[i]:
                res.append(ele)
                if len(res) == k:
                    return res
