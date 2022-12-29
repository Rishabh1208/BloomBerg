# brute force approach : everytime I have two choices whether to take it or not. O(2^n)
# DP could be o(N2) -- Not doing this.
# greedy o(nlogn) approach : subtracting city2 - city1 and then sort it.
def twoCitySchedCost(costs):
    diff = []
    for c1, c2 in costs:
        d = [c2-c1, c1, c2]
        diff.append(d)

    diff.sort()
    total = 0

    for i in range(len(diff)):
        if i < len(diff)//2:
            total += diff[i][2]
        else:
            total += diff[i][1]

    return total

# costs = [[10,20],[30,200],[400,50],[30,20]]
# TC: O(n2) SC: O(n)
def twoCitySchedCost(self, costs):
    memo = {}

    def dfs(i, a, b):
        if a == len(costs) // 2 and b == len(costs) // 2:
            return 0

        if i == len(costs) or a > len(costs) // 2 or b > len(costs) // 2:
            return float('inf')

        if (i, a, b) in memo:
            return memo[(i, a, b)]

        pickA = costs[i][0] + dfs(i+1, a+1, b)
        pickB = costs[i][1] + dfs(i+1, a, b+1)
        memo[(i, a, b)] = min(pickA, pickB)
        return memo[(i, a, b)]

    return dfs(0, 0, 0)
