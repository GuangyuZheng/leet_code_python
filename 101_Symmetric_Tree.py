# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _isSymmetric(self, left_subtree, right_subtree):
        if left_subtree is None and right_subtree is not None:
            return False
        if left_subtree is not None and right_subtree is None:
            return False
        if left_subtree is None and right_subtree is None:
            return True
        if left_subtree.val == right_subtree.val:
            return self._isSymmetric(left_subtree.left, right_subtree.right) and self._isSymmetric(
                    left_subtree.right, right_subtree.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is not None:
            return self._isSymmetric(root.left, root.right)
        else:
            return True
