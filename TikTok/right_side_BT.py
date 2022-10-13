import collections


def rightSide(root):
    # if root is None
    if root is None:
        return []

    res = []
    # maintainung queue
    q = collections.queue()
    # appending root to the queue
    q.append(root)

    # Till queue is empty
    while q:
        rightSide = None

        # iterating till the length of the queue.
        for i in range(len(q)):
            # poping the first element of the queue.
            node = q.popleft()

            # There might be chances that node in the queue could be null.
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        # again there migth be chances rightside is None because we initally initialize it to None. and there might be chances inside the for Loop we could pass if node:
        if rightSide:
            res.append(rightSide.val)
    return res
