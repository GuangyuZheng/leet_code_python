# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 1
        current_layer = [root]
        next_layer = []
        while len(current_layer) != 0:
            node = current_layer.pop(0)
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                next_layer.append(node.left)
            if node.right is not None:
                next_layer.append(node.right)
            if len(current_layer) == 0:
                current_layer = next_layer
                next_layer = []
                depth += 1
        return depth