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

# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

# arr = [[10000, 15], [50000, 20], [250000, 28], [500000, 37], [float('inf'), 42]]

def summaryRanges(arr, income):
    tax = prev = 0

    for amount, p in arr:
        if income >= amount:
            tax += (amount-prev) * (p/100)
            prev = amount
        else:
            tax += (income-prev) * (p/100)
            break

    return tax


arr = [[10000, 15], [50000, 20], [250000, 28],
       [500000, 37], [float('inf'), 42]]
income = 85000

print((summaryRanges(arr, income)))
