def search(self, nums, target):
    low = 0
    high = len(nums)-1
    # edge case [3] only 1 element in an array that's why low <= high instead of low < high
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        # left sorted portion
        if nums[mid] >= nums[low]:
            if nums[low] <= target and target < nums[mid]:
                high = mid-1
            else:
                low = mid + 1

        # right sorted portion
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
