def longestCommonPrefix(strs):
    if not strs:
        return ''
    minLetter, maxLetter, count = min(strs), max(strs), 0
    print(minLetter, maxLetter)
    for i in range(min(len(minLetter), len(maxLetter))):
        if minLetter[i] != maxLetter[i]:
            break
        else:
            count += 1
    return minLetter[:count]

# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["flow", "flo", "flower"]
print(longestCommonPrefix(strs))


# Approach1: Horizontal searching
# Approach2: Vertical searching
# Approach3: Find the max and min of string in the array and loop till min length of the string
#            and compare only minimum and maximum string
