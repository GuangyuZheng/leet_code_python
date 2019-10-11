# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is not None or p is not None and q is None:
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False

        condition1 = self.isSameTree(p.left, q.left)
        condition2 = self.isSameTree(p.right, q.right)
        return condition1 and condition2
