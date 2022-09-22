class ListNode:
    def __init__(self, val, minValue):
        self.val = val
        self.minValue = minValue
        self.next = None

class MinStack(object):

    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = ListNode(val, val)
        else:
            curr = ListNode(val, min(self.head.minValue, val))
            curr.next = self.head
            self.head = curr

    def pop(self):
        if self.head is not None:
            self.head = self.head.next

    def top(self):
        if self.head is not None:
            return self.head.val
        return -1

    def getMin(self):
        if self.head is not None:
            return self.head.minValue
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
