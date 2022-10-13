
# Preorder: [root,left,right]
# preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Note: You are not allowed to reconstruct the tree.

 
# Time complexity: o(n)
# space complexity: o(n) [because of splitting]
def isValidSerialization(self, preorder):
    # number of available slots
    slots = 1

    for node in preorder.split(','):
        # one node takes one slot
        slots -= 1

        # no more slots available
        if slots < 0:
            return False

        # non-empty node creates two children slots
        if node != '#':
            slots += 2

    # all slots should be used up
    return slots == 0

# Time complexity: o(n)
# space complexity: o(1)
def isValidSerialization(self, preorder: str) -> bool:
    # number of available slots
    slots = 1

    prev = None  # previous character
    for ch in preorder:
        if ch == ',':
            # one node takes one slot
            slots -= 1

            # no more slots available
            if slots < 0:
                return False

            # non-empty node creates two children slots
            if prev != '#':
                slots += 2
        prev = ch

    # the last node
    slots = slots + 1 if ch != '#' else slots - 1
    # all slots should be used up
    return slots == 0
