# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# time O(n)
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current_node = node
        next_node = node.next
        while next_node.next is not None:
            current_node.val = next_node.val
            current_node = next_node
            next_node = next_node.next
        current_node.val = next_node.val
        current_node.next = None


# time O(1)
class SolutionV2:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
