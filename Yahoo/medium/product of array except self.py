def productExceptSelf(self, nums):

    # Good solution as this might come up first in my mind instead of what submiited, 
    # the only difference is here I am appending instead of creating an array of same 
    # with initialzie 0.
    res = []

    acc = 1
    for n in nums:
        res.append(acc)
        acc *= n

    acc = 1
    for i in reversed(range(len(nums))):
        res[i] *= acc
        acc *= nums[i]

    return res
