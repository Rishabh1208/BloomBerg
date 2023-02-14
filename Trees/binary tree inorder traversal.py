
def inorderTraversal(root):
    # Iterative
    res, stack = [], []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
    
    
def inorderTraversal(root):

    # Recursive
    res = []

    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)

    helper(root)
    return res
