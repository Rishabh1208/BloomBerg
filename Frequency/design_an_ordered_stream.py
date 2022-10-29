# Design UDP:

# A Key (integer), value (string) pair is given at a time. It only prints value in sequence of
# ascending order of keys. If the key is not in order, it doesn’t print its string value and only
# prints the value until it sees the next key in order.

# When it goes through all the keys, it prints the remaining values in order if no value in the
# sequence is missing. Only one pair of key and value is given at a time. There is no list.
# ould anyone tell me what Leetcode problem is this? Thank you.

# Example:

#     1, "A"
#     2, "B"
#     3, "C"
#     7, "G"
#     4, "D"
#     6, "F"
#     5, "E"

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

# Problem Statement:
# An application is receiving UDP network data. Given the nature of UDP protocol, 
# data can be received out of order or can get lost over the network.
# With each piece of data however, we also receive an incremental sequence number 
# indicating the order of the data as it was sent out by the source.

# Design:
# Write a class called "Sequencer" which prints all received data to standard output in order, 
# according to the data's sequence number.

# Follow up: how would you make it space effiencient, time efficient?


# approach 1 - using list
# approach 2 - using hashmap
class OrderedStream:

    def __init__(self, n):
        self.values = [None] * n  # initialize an array of size n
        self.ptr = 0  # remember where the stream pointer is at

    def insert(self, idKey, value):

        # set the arr's 0-indexed value to the incoming value
        self.values[idKey-1] = value

        # Construct the next chunk by checking bounds, and ensuring value is not None
        chunk = []
        while self.ptr < len(self.values) and self.values[self.ptr]:
            chunk.append(self.values[self.ptr])
            self.ptr += 1  # update the pointer

        return chunk


class OrderedStream:
    def __init__(self, n):
        self.hashMap = {}
        self.ptr = 1

    def insert(self, idkey, value):
        self.hashMap[idkey] = value
        if idkey > self.ptr:
            return []

        result = []
        while self.ptr in self.hashMap:
            result.append(self.hashMap[self.ptr])
            del self.hashMap[self.ptr]  # To delete some memory
            self.ptr += 1

        return result
