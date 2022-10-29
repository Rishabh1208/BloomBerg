# https://leetcode.com/discuss/interview-question/1126383/Bloomberg-or-New-Grad-or-NY-or-Feb-2021-Onsite-Passed



# Q1: Similar to Collatz Conjecture (haven’t seen on LC before)
# somewhat close to sort integers by the power of two
# Starting from 1, generate a sequence - which denotes the operations used to reach the 
# target
# 	* multiple by 2
# 	* floor division by 3

# Example 1:
# # target = 1
# # output: ""
# # explanation: 1 (target) = 1, no operations needed

# Example 2:
# # target = 2 
# # output: "*"
# # explanation: 2 (target) = 1 * 2 

# Example 3:
# # target = 8 
# # output: "***"
# # explanation: 8 (target) = 1 * 2 * 2 * 2 

# Example 4:
# # target = 10 
# # output: "****/*"
# # explanation: 10 (target) = 1 * 2 * 2 * 2 * 2 // 3 * 2

# Example 5:
# # target = 3 
# # output: "****/*/"
# # explanation: 3 (target) = 1 * 2 * 2 * 2 * 2 // 3 * 2 // 3
# follow-up question - what if we call the method multiple times?
# code a solution for expanded scope
# follow-up question - code optimization for the expanded scope
# follow-up question - optimize it further