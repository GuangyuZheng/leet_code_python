# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if head is None:
            return head
        prev = head
        current = head.next
        while True:
            while current:
                if current.val == val:
                    current = current.next
                else:
                    break
            prev.next = current
            prev = current
            if current:
                current = current.next
            else:
                break
        return head

    # Recursion version
    def removeElementsV2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            head = head.next
        return head
