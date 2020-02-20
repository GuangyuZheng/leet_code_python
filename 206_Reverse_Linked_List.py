# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # Recursive Version
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        new_head = self.reverseList(head.next)
        if new_head:
            tmp = new_head
            while tmp.next:
                tmp = tmp.next
            tmp.next = head
            head.next = None
        else:
            new_head = head
        return new_head

    # recursive version
    def reverseListV2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = self.reverseListV2(head.next)
        head.next.next = head
        head.next = None
        return p

    # iteratively version
    def reverseListV3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev = None
        current = head
        while current:
            tp, tc = current, current.next
            current.next = prev
            prev = tp
            current = tc
        return prev


