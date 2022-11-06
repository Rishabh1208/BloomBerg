def singleNumber(self, nums):
    res = 0
    for n in nums:
        res = res ^ n
    return res

# XOR
# 1^1 = 0
# 0^0 = 0
# 0^1 = 1
# 1^0 = 1
# Therefore n^0 = n
