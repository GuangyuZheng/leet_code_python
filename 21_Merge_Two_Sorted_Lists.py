# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = None
        head = None
        while (l1 is not None) and (l2 is not None):
            min_value = min(l1.val, l2.val)
            new_node = ListNode(min_value)
            if current is None:
                head = new_node
            else:
                current.next = new_node
            current = new_node
            if min_value == l1.val:
                l1 = l1.next
            else:
                l2 = l2.next
        if l1 is not None:
            if current is None:
                head = l1
            else:
                current.next = l1
        if l2 is not None:
            if current is None:
                head = l2
            else:
                current.next = l2
        return head
