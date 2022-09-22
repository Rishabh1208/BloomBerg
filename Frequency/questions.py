# 1) https://leetcode.com/problems/find-bottom-left-tree-value/
# 2) Intertsing post to read - https://leetcode.com/discuss/interview-question/1047010/Bloomberg-Onsite-New-Grad-NYC-(Reject)
# 3) Simple LL Traversal and Delete Nth node from end of the list.
# 4) Deep Copy stuff and pretty challenging follow ups.
# 5) Simple question involving creating a graph and then seeing if there was a path from A -> B.
# 6) Second question was a dp problem involving coins.
# 7) https://leetcode.com/problems/evaluate-division/
# 8) https://leetcode.com/discuss/interview-question/1013880/Bloomberg-or-Phone-%2B-Onsite-or-Interview-Questions
# 9) https://leetcode.com/discuss/interview-question/1126383/Bloomberg-or-New-Grad-or-NY-or-Feb-2021-Onsite-Passed
# 10) https://leetcode.com/discuss/interview-question/1211023/Bloomberg-2021-New-Grad-Software-Engineer


# Give a stream of stock prices, design a data structure to support the following operations:

# StockSticker(int k) Initialize the size of the ticker.
# void addOrUpdate(String stock, double price) add or update the price of a stock to the data structure.
# List<Map.Entry<String, double>> top() return the top k price stocks and their current prices.

# class StockTicker:

#     def __init__(self, k):
#         self.prices = {}

#     def addorUpdate(self, stock, price):
#         self.prices[stock] = price

#     def topKPrices(self):


# Given two arrays A, B and a target v, find out two elements a and b (one from A and another from B) so that a+b = v
# A = [1,2,3,4]
# B = [2,3,7,8]
# target = 9


# Question was basically valid parantheses question in leetcode which followed by some follow-ups like "what happens if I want to invent some custom parantheses like "<>"?".
# I implemented hashmap for different paranthesis types using std::map.
# After that other enginner asked me some questions about time complexity of std::map and std::unordered_map in C++.
# I answered them for std::map as it is a binary search tree basically, but choked on describing how unordered_map has O(1) time complexity.
# Interviewee wanted me to describe how it is O(1) and what is hashing? but I couldn't properly.


# A Python set is implemented as a hash table with just `keys` and no `values` (or dummy values). That key is passed into a hash function, which returns a block address or index (of the base array on which the set is built).
# We know that any index can be accessed in O(1). And here, we are not accessing the `value` at the index, but we are, checking the `existence` of that index in our base array, which is, of course, O(1).
# But you may notice others saying the worst case for a lookup is O(n)!! How?

# Things get tricky here:
# Our hash function, which returns an index, can return the same index for 2 or more different `keys,` which is called a Hash Collision, and this will result in 2 keys allotted at the same index. What happens here?
# So basically, there are multiple ways to mitigate this. One of the standard methods is to allot a pointer towards a `linked list` at that index, and “those keys” with the same `index` are now members of a linked list, with each key stored in a node.
# (Generally, how linked list works).


# Task was very easy. We have tickers of stocks and many prices.
# We need to add them and then be able to take N oldest by ticker and N params.
# I think I choose right base structure Dictionary<string, XXX>
# To store stock prices per ticker name.
# But then I started to do something wrong. (below will be about XXX)
# I was very nervous becuase of interview and told that we need to use doubly linked list to store prices
# to be able to take oldest N prices with lower complexity. Inteviewer tried to give me advices. But i was in "flow" already:) and did not listen him:(
# Just interview finished I realized that I could use simple List of decimal to store prices i.e. Dictionary<string, List> instead of Dictionary<string, DoublePriceLinkedList>>

# And we know that to traverse down a linked list, we need O(i) time, where `i` is the length of the linked list (or the last element/ or the element to be searched).
# So suppose we get a collision at every key, and we end up with one `index` for every key. Thus all keys will be stored in a linked list in different nodes following the previous one.
# And our whole Hash Table is now `indeed` a linked list, to be precise:
# We end up with a block with a pointer that points towards “this” linked list.
# We have `n` items inside the linked list (which means all items) and to lookup an element that turned out to be the element in our last node inside the linked list, we have to traverse through the whole linked list and hence requiring O(n) steps.
# This is where we get the worst case of O(n) lookup.
# Still, such extreme collisions are infrequent and `impractical` in real life, and we generally have a lot of blocks to be allotted in our python implementation to prevent such collisions. So we say that our average algorithmic complexity is O(1)!
# I hope that helps!


def collatz(num, memo={1: 0}):
    if num in memo:
        return memo[num]

    if num % 2:
        res = 1 + collatz(3*num + 1, memo)
    else:
        res = 1 + collatz(num//2, memo)

    memo[num] = res

    return res
