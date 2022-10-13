# https://leetcode.com/discuss/interview-question/2335270/Bloomberg-Virtual-Interview-Question-2022

# the interviewer emphasized that executeOrder should be very quick, there is a high volume of these calls.
# He was satisfied with a hashTable (O(1)).

# For printTopNTrades I suggested sorting the keys of hashTable or using a minheap (both are O(NLogN)),
# he accepted both, and I was invited for the virtual onsite.


# Using a doubly linked list where we maintain a descending order by volume and a hashmap whose keys point to the node of the DLL?

# executeOrder() -> move/create a new node for trade and iterate through the DLL to place it accordingly. Time Complexity: O(N)
# printTopNTrades() -> iterate through the DLL from the start and print the top n nodes. Time Complexity : O(N)