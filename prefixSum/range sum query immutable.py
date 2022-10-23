class NumArray(object):

    def __init__(self, nums):
        self.prefixSum = []
        self.prefix = 0
        for i in nums:
            self.prefix += i
            self.prefixSum.append(self.prefix)

    def sumRange(self, left, right):
        if left-1 >= 0:
            return self.prefixSum[right] - self.prefixSum[left-1]
        return self.prefixSum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
