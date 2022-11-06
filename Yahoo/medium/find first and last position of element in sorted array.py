def FirstOccurence(self, arr, target):
        low = 0
        high = len(arr) - 1
        res = -1
        while(high >= low):
            mid = low + (high - low)//2
            if arr[mid] == target:
                res = mid
                high = mid-1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

def LastOccurence(self,arr,target):
    low = 0
    high = len(arr) - 1
    res  = -1
    while(high >=low):
        mid = low + (high - low)//2 
        if arr[mid] == target:
            res = mid
            low = mid+1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return res

def searchRange(self, nums, target):
    return [self.FirstOccurence(nums,target), self.LastOccurence(nums,target)]