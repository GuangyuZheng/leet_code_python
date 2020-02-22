# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        val = prev.next.val
        node = head.next

        while node is not None:
            if node.val != val:
                prev = prev.next
                if prev.next is None:
                    break
                val = prev.next.val
                node = node.next
            else:
                t_node = prev.next
                while t_node is not None:
                    if t_node.val == val:
                        t_node = t_node.next
                    else:
                        break
                prev.next = t_node
                if t_node is None:
                    break
                val = t_node.val
                node = t_node.next
        return dummy.next


# cleaner code version
class SolutionV2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next is not None and current.next.next is not None:
            if current.next.val == current.next.next.val:
                t_node = current.next
                while t_node is not None and t_node.next is not None and (t_node.val == t_node.next.val):
                    t_node = t_node.next
                current.next = t_node.next
            else:
                current = current.next

        return dummy.next
