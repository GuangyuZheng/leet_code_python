from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def help(in_start, in_end, post_start, post_end):
            assert in_end-in_start == post_end-post_start
            if in_start > in_end:
                return None
            head = TreeNode(postorder[post_end])
            in_pos = inorder.index(postorder[post_end])
            head.right = help(in_pos+1, in_end, post_end-(in_end-in_pos), post_end-1)
            head.left = help(in_start, in_pos-1, post_start, post_end-(in_end-in_pos)-1)
            return head
        n = len(inorder)
        return help(0, n-1, 0, n-1)
