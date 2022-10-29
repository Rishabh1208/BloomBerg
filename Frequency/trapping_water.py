# 3 approaches 
# 1st --> O(N^2), 2nd --> O(N) , o(N), 3rd --> o(N)
def trap(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
            l += 1
        else:
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
            r -= 1
    return res
