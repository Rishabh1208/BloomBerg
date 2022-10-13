# https://leetcode.com/discuss/interview-question/2595082/Bloomberg-Phone-Interview-SSE-or-NYC


# What data structure would you use to store the federal tax slab?

# Range - Tax Rate
# 0-10000 - 15%
# 10001-50000 - 20%
# 50001-250000 - 28%
# 250001-500000 - 37%
# 500001 and above - 42%
# (Not the exact values)

# Input - 85000
# Output - 10000 * 0.15 + 40000 * 0.20 + 35000 * 0.28 = 19300
# 1) First think of hashmap then come up with array with tuples and then 2d array.
# brackets = [0,10000, 15%]
def calculateTax(brackets, income):
    tax = prev = 0
    for _, upper, p in brackets:
        if income >= upper:
            tax += (upper - prev) * p / 100
            prev = upper
        else:
            tax += (income - prev) * p / 100
            return tax
    return tax
