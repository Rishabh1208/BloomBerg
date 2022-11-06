def findDuplicate(self, nums):
    for num in nums:
        cur = abs(num)
        if nums[cur] < 0:
            duplicate = cur
            break
        nums[cur] = -nums[cur]

    # Restore numbers
    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return duplicate
