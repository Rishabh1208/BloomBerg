def moveZeroes(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[count] = nums[count], nums[i]
            count += 1
            
nums = [0,1,0,3,12]
