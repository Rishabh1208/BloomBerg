from collections import deque

def rightSideView(self, root):  # same as level order traversal
    result = []
    q = deque()
    if root:
        q.append(root)

    while q:
        node = None
        for i in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        if node:
            result.append(node.val)
    return result
