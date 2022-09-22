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
        if i < diff//2:
            total += diff[i][2]
        else:
            total += diff[i][1]
            
    return total
            
            
