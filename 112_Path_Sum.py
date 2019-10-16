# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == sum
        elif root.left is not None and root.right is None:
            return self.hasPathSum(root.left, sum - root.val)
        elif root.left is None and root.right is not None:
            return self.hasPathSum(root.right, sum - root.val)
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
