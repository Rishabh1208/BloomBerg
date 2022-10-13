# https://leetcode.com/discuss/interview-question/407179/Bloomberg-or-Remove-array-elements-in-given-index-ranges

# Remove array elements in given index ranges
# Input: array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
# Output: [-8, 3, -5, 29, 43, 76, 73, 76]

# def remove_idxs(arr, ranges):
#     max_size = len(arr)
#     lookup_arr = [0] * max_size
#     for range in ranges:
#         start, end = range[0], range[1]
#         # why not just +1 or -1
#         # because we may have overlapping ranges
#         # like [5,8], [5, 10]
#         if start < max_size:
#             lookup_arr[start] += 1
#         if end < max_size:
#             lookup_arr[end] -= 1
#     print(lookup_arr)

#     sum_so_far = 0
#     result = []
#     for idx, num in enumerate(arr):
#         sum_so_far += lookup_arr[idx]
#         if sum_so_far == 0:
#             result.append(num)
#     return result


def remove_ints_from_array(array, ranges):
    for start, stop in ranges:
        if start >= len(array):
            continue
        for i in range(start, stop):
            array[i] = float('inf')
    result = []
    for value in array:
        if value != float('inf'):
            result.append(value)
    return result


print(remove_ints_from_array([-8, 3, -5, 1, 51, 56, 0, -5, 29, 43,
      78, 75, 32, 76, 73, 76], [[5, 8], [10, 13], [3, 6], [20, 25]]))


arr = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
print(remove_idxs(arr, ranges))
