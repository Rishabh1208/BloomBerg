def kthSmallest(self, root, k):
    #         stack = []
    #         curr = root
    #         n = 0

    #         while curr and stack:
    #             while curr:
    #                 stack.append(curr)
    #                 curr = curr.left

    #             curr = stack.pop()
    #             n+=1
    #             if n == k:
    #                 return curr.val

    #             curr = curr.right

    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right
