# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        lt_head = None
        lt_tail = None
        ge_head = None
        ge_tail = None
        node = head
        while node is not None:
            if node.val < x:
                if lt_head is None:
                    lt_head = node
                    lt_tail = node
                else:
                    lt_tail.next = node
                    lt_tail = node
            else:
                if ge_head is None:
                    ge_head = node
                    ge_tail = node
                else:
                    ge_tail.next = node
                    ge_tail = node
            node = node.next
        if lt_tail is not None:
            lt_tail.next = ge_head
            if ge_tail is not None:
                ge_tail.next = None
            return lt_head
        else:
            ge_tail.next = None
            return ge_head


# dummy node version, cleaner code
class SolutionV2:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        lt_head = lt = ListNode(0)
        ge_head = ge = ListNode(0)
        node = head
        while node is not None:
            if node.val < x:
                lt.next = node
                lt = node
            else:
                ge.next = node
                ge = node
            node = node.next

        lt.next = ge_head.next
        ge.next = None

        return lt_head.next
