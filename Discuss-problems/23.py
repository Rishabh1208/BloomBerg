# https://leetcode.com/discuss/interview-question/1092379/Bloomberg-or-2021-Software-Engineer-or-NYC-Offer


# Given a balanced string containing letters a-z and brackets "()[]{}", return the deepest nested substrings
# Example: "a[bc]def{cd}" -> ["bc","cd"]

# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses


# One way to approach would be to keep a List<List<String>> where each sublist are strings
# from a certain depth. You loop through the input string keeping track of a depth pointer.
# Whenever you encounter one of the opening brackets, you increase the depth and start
# appending characters to that sublist (you will need to create a sublist if you haven't
# visited that depth before), then decrease the depth whenever you come across one of the
# closing brackets. Then you just simply return the that sublist.

# There's some memory optimizations such as not keeping track of all sublists
# (when you encounter a new depth, empty the old list and start saving elements
#  to the new list)

from collections import defaultdict


def maximumDepth(string):
    count = 0
    openSet = set(["(", "{", "["])
    closeSet = set(["}", "]", ")"])
    maxCount = 0
    preMap = defaultdict(list)
    result = []
    for ele in string:
        if ele in openSet:
            count += 1

            maxCount = max(maxCount, count)
        elif ele in closeSet:
            count -= 1

        else:
            preMap[count].append(ele)

    for key, value in preMap.items():
        if maxCount == key:
            result += value
    return result


string = "a[b(c)t]def{cd}"
print(maximumDepth(string))
