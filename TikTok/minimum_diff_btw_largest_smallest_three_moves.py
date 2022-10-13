import heapq

# Intuition
# If we can do 0 move, return max(A) - min(A)
# If we can do 1 move, return min(the second max(A) - min(A), the max(A) - second min(A))
# and so on.

# Explanation
# We have 4 plans:

# kill 3 biggest elements
# kill 2 biggest elements + 1 smallest elements
# kill 1 biggest elements + 2 smallest elements
# kill 3 smallest elements

# Example

# A = [1,5,6,13,14,15,16,17]
# n = 8

# Case 1: kill 3 biggest elements

# All three biggest elements can be replaced with 14
# [1,5,6,13,14,15,16,17] -> [1,5,6,13,14,14,14,14] == can be written as A[n-4] - A[0] == (14-1 = 13)

# Case 2: kill 2 biggest elements + 1 smallest elements

# [1,5,6,13,14,15,16,17] -> [5,5,6,13,14,15,15,15] == can be written as A[n-3] - A[1] == (15-5 = 10)

# Case 3: kill 1 biggest elements + 2 smallest elements

# [1,5,6,13,14,15,16,17] -> [6,6,6,13,14,15,16,16] == can be written as A[n-2] - A[2] == (16-6 = 10)

# Case 4: kill 3 smallest elements

# [1,5,6,13,14,15,16,17] -> [13,13,13,13,14,15,16,17] == can be written as A[n-1] - A[3] == (17-13 = 4)

# Answer is minimum of all these cases!


# If the size <= 4, then just delete all the elements and either no or one element would be left
# giving the answer 0.
# else sort the array
# there are 4 possibilities now:-

# delete 3 elements from left and none from right
# delete 2 elements from left and one from right
# and so on.. now just print the minima.
# Time complexity: O(nlogn)
def minDifference(nums):
    if len(nums) <= 4:
        return 0
    nums.sort()
    # delete all the 3 elements from the right
    a = nums[-4] - nums[0]
    print(a)
    # delete 2 elemenst from right and 1 element from left.
    b = nums[-3] - nums[1]
    print(b)
    # delete 1 element from right and 2 element from left.
    c = nums[-2] - nums[2]
    print(c)
    # delete all elements from the left.
    d = nums[-1] - nums[3]
    print(d)

    return min(a, b, c, d)


nums = [1, 5, 6, 13, 14, 15, 16, 17]
print(minDifference(nums))

# Time compelxity: O(nlogk)
def minDifference(self, nums):
    heapq.heapify(nums)                 # O(n) time
    small = heapq.nsmallest(4, nums)    # O(logn) time
    large = heapq.nlargest(4, nums)     # O(logn) time
    large.reverse()                     # O(n) time
    return min(x-y for x, y in zip(large, small))  # O(1) time
