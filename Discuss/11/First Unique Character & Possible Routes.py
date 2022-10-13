# # https://leetcode.com/discuss/interview-question/440136/Bloomberg-or-Phone-or-First-Unique-Character-and-Possible-Routes

# It was pretty easy got asked 2 questions, one similar to LRU cache
# 2nd one similiar to Two sum find array pairs that add up to target value

# Other Questions which I didnt do well in:
# how does python store dictionaries? what key types are ok in python (I told him i only used strings and integers)

# Given a Subway system where the customer can swipe in his card to check in and swipe out his card to 
# check out at destination station, get the average time needed to travel between any 2 stations. 
# and I should save customer Id, create swipeIn and swipeOut functions and another to get the average

# Follow up Question
# 1.what if a person lost his card how can you utilize that fact?
# Ans: I told him I wouldnt store his custID anymore so I can use an orderdict with any capacity I want for example 500K persons and if i get a new person I remove the oldest entry from my OrderedDict

# What if route didnt exisits between 2 stations?
# Ans: I told him thats why I returned -1 he told me its not idicative I told him we dont have negative time, but i can instead return a string"No Route"