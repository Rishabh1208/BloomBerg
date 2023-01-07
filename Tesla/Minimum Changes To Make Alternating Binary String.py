
# We have two options, how the alternating string looks like.

# starting with "0" it is "01010101010101010....."
# starting with "1" it is "101010101010101010...."
# On all even positions are ones and on the odd positions are zeros or vice versa.

# We are comparing the given string s with these two options and counting number of differencies.
# Return the better option.

def minOperations(s):
    answ1 = answ0 = 0
    for i in range(len(s)):
        z = str(i % 2)
        answ1 += s[i] != z
        answ0 += s[i] == z
    return min(answ0, answ1)

s = "0010000"
print(minOperations(s))
