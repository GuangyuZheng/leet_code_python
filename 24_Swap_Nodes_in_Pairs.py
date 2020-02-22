# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        first = head
        second = head.next

        while second is not None:
            tmp_node = second.next
            prev.next = second
            second.next = first
            first.next = tmp_node

            if tmp_node is None:
                break

            prev = first
            tmp_first = first
            first = second.next.next
            second = tmp_first.next.next

        return dummy.next


# iteration clearly version
class SolutionV2:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while head is not None and head.next is not None:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next


# recursion version
class SolutionV3:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second
