def kthSmallest(self, root, k):
    stack = []
    curr = root
    n = 0
    while True:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        n += 1

        if n == k:
            return curr.val
        curr = curr.right
