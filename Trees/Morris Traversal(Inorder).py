class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Morris(root):
    # Set current to root of binary tree
    curr = root

    while curr is not None:
        if curr.left is None:
            print(curr.data)
            curr = curr.right
        else:
            # Find the previous (prev) of curr
            prev = curr.left
            while prev.right is not None and prev.right != curr:
                prev = prev.right

            # Make curr as right child of its prev
            if prev.right is None:
                prev.right = curr
                curr = curr.left

            # fix the right child of prev
            else:
                prev.right = None
                print(curr.data)
                curr = curr.right


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
