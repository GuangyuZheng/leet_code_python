# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # save height at first version
    def getHeight(self, root:TreeNode):
        if root is None:
            return 0
        else:
            result = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            root.height = result
            return result

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            self.getHeight(root)
            if root.left is None:
                left_height = 0
            else:
                left_height = root.left.height
            if root.right is None:
                right_height = 0
            else:
                right_height = root.right.height
            if abs(left_height-right_height) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False

    # stop early version
    def depth(self, root: TreeNode):
        if root is None:
            return 0
        left = self.depth(root.left)
        if left == -1:
            return -1
        right = self.depth(root.right)
        if right == -1:
            return -1
        else:
            return 1 + max(left, right) if abs(left - right) <= 1 else -1

    def isBalancedV2(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

