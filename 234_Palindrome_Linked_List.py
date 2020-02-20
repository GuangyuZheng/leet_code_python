# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# time O(n) space O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]


# time O(n) space O(1)
class SolutionV2:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        mid = self.findMiddle(head)
        mid = mid.next
        mid = self.reverse(mid)
        f_node = head
        mid_node = mid

        while mid_node is not None:
            if f_node.val != mid_node.val:
                return False
            f_node = f_node.next
            mid_node = mid_node.next
        return True

    def findMiddle(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        previous = None
        node = head
        while node.next is not None:
            tmp_node = node.next
            node.next = previous
            previous = node
            node = tmp_node
        node.next = previous
        return node
