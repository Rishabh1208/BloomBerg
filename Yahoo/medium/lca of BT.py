def lowestCommonAncestor(self, root, p, q):
    if root is None or root == p or root == q:
        return root
    leftChild = self.lowestCommonAncestor(root.left, p, q)
    rightChild = self.lowestCommonAncestor(root.right, p, q)
    if leftChild and rightChild:
        return root
    return leftChild or rightChild
