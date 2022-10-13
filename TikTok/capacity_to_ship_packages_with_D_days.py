# weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Binary search, left would be max(weights) and right would be sum(weights), why left would be max of weights.
# Because if we choose 9, we couldn't ship 10 because it will take infinity amount of time.

def shipWithinDays(weights, days):
    def feasible(capacity):
        day = 1
        total = 0
        for weight in weights:
            total += weight
            
            if total > capacity:  # too heavy, wait for the next day
                print("total", total)
                print("weight", weight)
                total = weight
                day += 1
                if day > days:  # cannot ship within D days
                    return False
        return True

    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        print("mid", mid)
        if feasible(mid):
            # since we have to find least weight capacity, there might be a chances we could find it in more optimal way.
            right = mid
        else:
            left = mid + 1
    return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

shipWithinDays(weights, days)
