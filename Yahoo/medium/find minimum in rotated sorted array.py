def findMin(self, nums):
    low = 0
    high = len(nums)-1
    if nums[low] <= nums[high]:
        return nums[low]
    
    while low <= high:
        mid = (low + high)//2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid-1] > nums[mid]:
            return nums[mid]
        elif nums[low] < nums[mid]:
            low = mid+1
        elif nums[mid] < nums[high]:
            high = mid-1
