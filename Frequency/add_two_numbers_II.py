# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        s1, s2 = 0, 0

        while l1 != None:
            s1 = s1*10+l1.val
            l1 = l1.next

        while l2 != None:
            s2 = s2*10+l2.val
            l2 = l2.next

        dummylist = dummy = ListNode(0)

        for i in str(s1+s2):
            dummy.next = ListNode(i)
            dummy = dummy.next

        return dummylist.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # find the length of both lists
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next
            n1 += 1
        while curr2:
            curr2 = curr2.next
            n2 += 1

        # parse both lists
        # and sum the corresponding positions
        # without taking carry into account
        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

        # take the carry into account
        # to have all elements to be less than 10
        # 10->10->3 --> 0->1->4 --> 4->1->0
        curr1, head = head, None
        carry = 0
        while curr1:
            # current sum and carry
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the list
            curr1 = curr1.next

        # add the last carry
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return temp

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        temp = None
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
            newNode.next = temp
            temp = newNode
        return temp
