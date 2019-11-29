from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        assert len(preorder) == len(inorder)
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        head = TreeNode(preorder[0])
        idx_inorder = inorder.index(preorder[0])
        head.left = self.buildTree(preorder[1:1 + idx_inorder], inorder[0:idx_inorder])
        head.right = self.buildTree(preorder[1 + idx_inorder:], inorder[1 + idx_inorder:])
        return head
