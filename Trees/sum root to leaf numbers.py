def sumNumbers(self, root):
    return self.pathToLeaf(root, 0)


def pathToLeaf(self, root, pathNumbers):
    if root is None:
        return 0
    pathNumbers = pathNumbers*10 + root.val
    if not root.left and not root.right:
        return pathNumbers
    return self.pathToLeaf(root.left, pathNumbers) + self.pathToLeaf(root.right, pathNumbers)
