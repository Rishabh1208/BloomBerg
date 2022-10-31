# Target Sum : Given an array of non negative numbers and a target integer return 
# TRUE if you can
# generate the number from the arrray using any subset of the array.

def targetSum(arr, target):
    memo = {}

    def dfs(i, target):
        if (i, target) in memo:
            return memo[(i, target)]
        if target == 0:
            return True
        if i == 0:
            if arr[i] == target:
                return True
            return False
        notPick = dfs(i-1, target)
        pick = dfs(i-1, target-arr[i])
        flag = notPick or pick
        memo[(i, target)] = flag
        print(memo)
        return memo[(i, target)]

    return dfs(len(arr)-1, target)


arr = [4, 1, 0, 3, 2, 5]
target = 5

print(targetSum(arr, target))
