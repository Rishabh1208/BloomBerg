
def flatten(self, root):

    def dfs(root):
        if not root:
            return None

        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        if root.left:  # we only care about leftTail
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        tail = rightTail or leftTail or root
        return tail
    dfs(root)

# SC: O(1) Morris Traversal
def flatten(root):

    # Handle the null scenario
    if not root:
        return None

    node = root
    while node:

        # If the node has a left child
        if node.left:

            # Find the rightmost node
            rightmost = node.left
            while rightmost.right:
                rightmost = rightmost.right

            # rewire the connections
            rightmost.right = node.right
            node.right = node.left
            node.left = None

        # move on to the right side of the tree
        node = node.right
