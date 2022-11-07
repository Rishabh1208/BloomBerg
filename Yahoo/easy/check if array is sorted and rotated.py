def check(self, nums):
    res = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            res += 1
    return res <= 1
