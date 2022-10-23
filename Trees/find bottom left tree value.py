from collections import deque


def findBottomLeftValue(self, root):
    q = deque([root])
    node = None
    while q:
        # In Python variable is function scoped not block scope
        node = q.popleft()

        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

    return node.val
