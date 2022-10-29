# https://leetcode.com/discuss/interview-question/1775399/Bloomberg-or-Phone-or-Get-Maximum-Value-of-Neighbor-values-in-an-array-of-integers


# I had this problem on my interview with Bloomberg. It is easily solved in O(N),
# but it is required to solve it in O(1) (all following functions).

# Build your own data structure which does the following functions:

# add(integer) -> add a new integer.
# getAll() -> return all elements in same insertion order.
# deleteLast() -> delete the last inserted element.
# getMaximum() -> return the maximum value of all elements.
# getMaximumNeighbourValues() -> return the maximum value of two consecutive elements.
# Example:
# [7, 3, 1, 10]: maxValue=10, maxNeighborsValue=11
# deleteLast -> [7, 3, 1]: maxValue=7, maxNeighborsValue=10
# add(2) -> [7, 3, 1, 2]: maxValue=7, maxNeighborsValue=10
# add(8) -> [7, 3, 1, 2, 8]: maxValue=8, maxNeighborsValue=10

# Solution:
# I came up to solve to first four functions in O(1). I used an arrayList to store the elements
# (to keep its order while insertion), and I used a LinkedHashMap to store the element as a key,
# and its occurrences as a value (that way, I kept the order to see which element is deleted,
# and I kept if maximum value should be modified -> takes the second last element in the map).
# That way, all functions have complexity O(1).

# But the fifth function is still unclear for me!

# class minStack:

#     def __init__(self):
#         self.stack = []
#         self.max = {0: float("-inf")}
#         self.nei = {}

#     def add(self, val):
#         self.stack.append(val)
#         cur_size = len(self.stack)
#         pre_max = self.max[cur_size-1]
#         self.max[cur_size] = max(pre_max, val)
#         if cur_size > 2:
#             pre_nei = self.nei[cur_size-1]
#             self.nei[cur_size] = max(pre_nei, val+self.stack[-2])
#         elif cur_size == 2:
#             self.nei[cur_size] = val+self.stack[-2]

#     def delete(self):
#         self.stack.pop()

#     def get_max(self):
#         cur_size = len(self.stack)
#         return self.max[cur_size]

#     def getMaxnei(self):
#         cur_size = len(self.stack)
#         return self.nei[cur_size]


# p = minStack()
# p.add(7)
# print(p.stack, p.max, p.nei)
# p.add(3)
# print(p.stack, p.max, p.nei)


class MinStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)  # [7,3]

        if not self.max_stack:
            self.max_stack.append([x, 0])  # [[7,7]]

        elif x > self.max_stack[-1][0]:
            SumOfTwo = x + self.stack[-2]
            SumOfTwo = max(SumOfTwo, self.max_stack[-1][1])
            self.max_stack.append([x, SumOfTwo])

        else:
            maxValue = self.max_stack[-1][0]
            SumOfTwo = x + self.stack[-2]
            SumOfTwo = max(SumOfTwo, self.max_stack[-1][1])
            self.max_stack.append([maxValue, SumOfTwo])

    def pop(self):
        if self.stack:
            self.max_stack.pop()
            return self.stack.pop()
        return -1

    def top(self):
        return self.stack[-1]

    def getMax(self):
        return self.max_stack[-1][0]

    def getMaxConsecutiveNeigh(self):
        return self.max_stack[-1][1]


p = MinStack()
p.push(7)
print(p.stack, p.max_stack)
p.push(3)
print(p.stack, p.max_stack)
p.push(1)
print(p.stack, p.max_stack)
p.push(10)
print(p.stack, p.max_stack)
print(p.getMaxConsecutiveNeigh())
p.pop()
print(p.stack, p.max_stack)
p.push(2)
print(p.stack, p.max_stack)
p.push(11)
print(p.stack, p.max_stack)
