

# https://leetcode.com/discuss/interview-question/1580252/Bloomberg-New-Grad-SWE-or-Phone-Interview-or-Counting-times-cars-will-pass-by-each-other

# Interview started with basic introduction (talked about myself and the favorite project that I worked
# on), then went to the HackerRank link provided to work on a coding challenge

# The question:

# Interviewer drew out the illustration exactly as shown below
# <----- 0-----0--0----
# ----1-----1--------1->

# On a 2 ways lane, there are cars driving west-bound (0) and cars driving east-bound (1),
# write a function that returns the amount of times that the cars will pass by each other.

# The above illustration was turned into an array [1,0,1,0,0,1] as input and should return 5
# (first "1" will drive by 3 "0", second will drive by 2, and third will drive by 0).

def time(arr):
    countOfZero = 0
    for ele in arr:
        if ele == 0:
            countOfZero += 1

    result = 0
    for ele in arr:
        if ele == 1:
            result += countOfZero
        else:
            countOfZero -= 1
    return result


arr = [1, 0, 1, 0, 0, 1]
print(time(arr))


# I think this can be done in O(n) time with O(1) space
# if we traverse from right and store the number corresponding to each one, for example:
# [1,0,1,0,0,1]
# if we start with j = 5, zeros = 0
# now as we move to left increase the count of zero, when we reach j = 2, zero = 2
# similarly when we reach j = 0, zero = 3

# Maintain a sum that will be updated as sum+=zero whenever we see 1.
# For above example we will add zero to sum when we reach j =5,2,0.
