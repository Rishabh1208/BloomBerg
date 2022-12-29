
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    temp = dummy
    carry = 0
    while l1 or l2 or carry:
        total = 0
        if l1:
            total += l1.val
            l1 = l1.next

        if l2:
            total += l2.val
            l2 = l2.next
        total += carry
        carry = total/10
        newNode = ListNode(total % 10)
        temp.next = newNode
        temp = newNode
    return dummy.next
