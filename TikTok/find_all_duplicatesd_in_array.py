def findDuplicates(self, nums):

    # Approach1 Take a set and then see.
    # Approach2 Imp. point to remember 1<= arr[i] <= n
    res = []
    for i in range(len(nums)):
        index = abs(nums[i])-1
        if nums[index] < 0:
            res.append(index+1)
        else:
            nums[index] = -nums[index]
    return res
