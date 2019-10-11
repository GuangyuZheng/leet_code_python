# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current_val = head.val
        prev = head
        current = head.next
        while current is not None:
            if current.val == current_val:
                prev.next = current.next
                current = current.next
            else:
                current_val = current.val
                prev = current
                current = current.next
        return head
