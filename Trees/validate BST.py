class Solution(object):
    def isValidBST(self, root):
        def validate(root, low, high):
            if root is None:
                return True
            if low >= root.val or high <= root.val:
                return False
            return validate(root.right, root.val, high) and validate(root.left, low, root.val)
        return validate(root, float('-inf'), float('inf'))
# class Solution(object):
    # def isValidBST(self, root):
    #     if root is None:
    #         return True
    #     if root and not root.left and not root.right:
    #         return True
    #     if root.left and root.val <= root.left.val or root.right and root.val >= root.right.val:
    #         return False
    #     return self.isValidBST(root.left) and self.isValidBST(root.right)
