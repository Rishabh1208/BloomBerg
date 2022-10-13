# https://leetcode.com/discuss/interview-question/2602533/Bloomberg-or-Phone-Interview-or-New-Grad-or-NYC

# Interviewer Introduced themself then asked why bloomberg. Followed by asking my biggest technical 
# challenge. (Interviewer had my resume on hand)

# First Problem: A process tree has crashed and you are given a sequence of it's nodes in random order, 
# each representing a process and possible child(s). Each node has at most two child process. 
# Find the root process node
# each node is represented as "Process ID: Children"
# Input:
# {5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}

#  			1
#  		/      \
#  	2            3
#  /     \          / 
#  4     5         6
# Output: 1

# Second Problem: Word Break ii