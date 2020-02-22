# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for i in range(n - 1):
            fast = fast.next

        prev = None
        while fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev is not None:
            prev.next = slow.next
        else:
            head = slow.next
        return head


# dummy node version
class SolutionV2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy
        for i in range(n+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
