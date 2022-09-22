# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Recursion
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail
    
# Iteration
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
