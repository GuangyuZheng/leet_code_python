# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        quick = head
        slow = head

        while True:
            if quick is None:
                return False
            quick = quick.next
            if quick is None:
                return False
            quick = quick.next

            slow = slow.next

            if slow == quick:
                return True
