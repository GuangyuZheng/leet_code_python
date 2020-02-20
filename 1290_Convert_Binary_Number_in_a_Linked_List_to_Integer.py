# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        node = head
        while node is not None:
            # result = result * 2 + node.val
            result = (result << 1) + node.val
            node = node.next
        return result
