# nums = [1,1,1], k = 2
def subarraySum(self, nums, k):
    freq = {}
    count = 0
    ksum = 0
    freq[0] = 1
    for ele in nums:
        ksum += ele
        if ksum - k in freq:
            count += freq[ksum-k]
        freq[ksum] = freq.get(ksum, 0) + 1
    return count
