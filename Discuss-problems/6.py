# There are several trades and trades have associated volumes as given below:

# Trade Volume
# A     200
# B     1000
# C     5
# D     1
# D     2
# D     3
# We have to perform below opearations based on the requirement.
# Operation 1: executeOrder(string trade, int volume)
# -If we have new trade, it should be added in the records.
# -If an existing trade comes with some volume, the new volume should be added in existing volume for that trade.

# Operation 2: printTopNTrades(int N)
# - this should print top N trades in descending order of thier volumes.

# In above example:
# 1. Operation 1: printTopNTrades(3)
# - should print (B, 1000), (A, 200), (D, 6)
# 2. Operation 2: executeOrder("E", 300)
# 3. Operation 3: printTopNTrades(3)
# - should print (B, 1000), (E, 300), (A, 200)

# My approach was to create hashmap and sort it by the volume in printTopNTrades opearation,
# but the time complexity goes O(nlogn) where n is number of trades. I also tried to use priority queue,
# but no luck with the time complexity. How can we reduce the time complexity to O(n)?


# Design a leaderboard.

# Using a doubly linked list where we maintain a descending order by volume and a hashmap
# whose keys point to the node of the DLL?

# executeOrder() -> move/create a new node for trade and iterate through the DLL to place it accordingly. Time Complexity: O(N)
# printTopNTrades() -> iterate through the DLL from the start and print the top n nodes. Time Complexity : O(N)
