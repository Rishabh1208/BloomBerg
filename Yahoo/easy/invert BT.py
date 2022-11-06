
def invertTree(self, root):
    if root is None:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root


def invertTree(self, root):
    if root is None:
        return None

    # root.right = self.invertTree(root.left) [ This doesn't work because we have to swap and we are not swapping here.]
    rightSubTree = self.invertTree(root.left)
    # root.left = self.invertTree(root.right)
    leftSubTree = self.invertTree(root.right)
    root.right = rightSubTree
    root.left = leftSubTree
    return root
