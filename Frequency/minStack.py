
# using two stacks
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# using one stack , storing tuple (x, minValue)
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        minValue = self.getMin()
        if minValue == None or val < minValue:
            minValue = val
        self.stack.append((val, minValue))

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]

#  using linked list


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
