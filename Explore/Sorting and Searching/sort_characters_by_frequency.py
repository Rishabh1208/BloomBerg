

from collections import Counter


def frequencySort(self, s):
    nums = list(s)
    arr = [[] for i in range(len(nums)+1)]
    res = []
    freq = Counter(s)
    for key, value in freq.items():
        arr[value].append(key*value)
    for i in range(len(arr)-1, 0, -1):
        if arr[i]:
            for ele in arr[i]:
                res.append(ele)
    return "".join(res)

# Approach above is Bucket sort that takes O(n)
# Normal sorting approach is below commented but the key point to take
# from the below approach is to how to use lambda sort with mutiple
# key paramaters.


#         nums = list(s)
#         freq = Counter(nums)
#         nums.sort(key = lambda x: (freq[x],x), reverse= True)
#         print(nums)
#         return "".join(nums)
