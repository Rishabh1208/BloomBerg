# https://leetcode.com/discuss/interview-question/1599164/Bloomberg-or-OA-(via-Google-Meet-video)-or-Design-an-Ordered-Stream


# Design UDP:

# A Key (integer), value (string) pair is given at a time. It only prints value in sequence of 
# ascending order of keys. If the key is not in order, it doesn’t print its string value and only 
# prints the value until it sees the next key in order.

# When it goes through all the keys, it prints the remaining values in order if no value in the 
# sequence is missing. Only one pair of key and value is given at a time. There is no list. 
# Could anyone tell me what Leetcode problem is this? Thank you.

# Example:

# 1, "A"
# 2, "B"
# 3, "C"
# 7, "G"
# 4, "D"
# 6, "F"
# 5, "E"
# It prints:
# A
# B
# C
# Doesn't print anything for 7
# D
# Doesn't print anything for 6
# E
# F
# G

# The interview was last month (October 2021).
