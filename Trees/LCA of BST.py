def lowestCommonAncestor(self, root, p, q):
    if root is None or root == p or root == q:
        return root
    if root.val > max(p.val, q.val):
        return self.lowestCommonAncestor(root.left, p, q)
    elif root.val < min(p.val, q.val):
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root
