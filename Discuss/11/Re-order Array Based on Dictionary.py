# # https://leetcode.com/discuss/interview-question/413734/Bloomberg-or-Re-order-Array-Based-on-Dictionary


# Consider a vector of employees with a name and their title:
# [<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

# And a dictionary where the keys report to the values:
# {[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

# Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, however the dictionary only contains the title orderings.

# Sample output:
# [<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

# Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, which is manager. They can also be in either order in this case.
