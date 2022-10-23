# BFS space --> o(N)
from collections import deque


def connect(self, root):
    if not root:
        return
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)

# BFS space --> O(1)


def connect(self, node):
    curr, nxt = node, node.left if node else None

    while curr and nxt:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left

        curr = curr.next
        if not curr:
            curr = nxt
            nxt = curr.left

    return node
