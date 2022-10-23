

def countPartitions(arr, d):

    total = sum(arr)
    diff = total - d
    if diff < 0 or diff % 2 == 1:
        return 0
    target = (total - d) // 2

    def dfs(i, tar):

        if tar == 0:
            return 1

        if i == 0:
            if arr[i] == tar:
                return 1
            return 0

        notPick = dfs(i-1, tar)
        pick = 0
        if target >= arr[i]:
            pick = dfs(i-1, tar-arr[i])
        return notPick + pick

    return dfs(len(arr)-1, target)


arr = [5, 2, 5, 1]
d = 3

print(countPartitions(arr, d))
