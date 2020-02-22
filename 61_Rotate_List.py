# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# reverse version
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        l = self.getLen(head)
        k = k % l

        if k == 0:
            return head

        reverse_head, reverse_tail = self.reverse(head)

        count = 0
        first_part_last = reverse_head
        while count < k - 1:
            first_part_last = first_part_last.next
            count += 1
        second_part_first = first_part_last.next
        first_part_last.next = None

        new_head, new_first_part_tail = self.reverse(reverse_head)

        new_first_part_tail.next = self.reverse(second_part_first)[0]

        return new_head

    def getLen(self, head):
        node = head
        l = 0
        while node is not None:
            l += 1
            node = node.next
        return l

    def reverse(self, head):
        if head is None or head.next is None:
            return head, head
        prev = None
        current = head

        while current is not None:
            t_c = current.next
            current.next = prev
            prev = current
            current = t_c
        return prev, head


# Ring version
class SolutionV2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        l = 0
        prev = None
        node = head
        while node is not None:
            prev = node
            node = node.next
            l += 1
        k = k % l

        tail = prev
        tail.next = head

        step = l - k
        node = head
        count = 0
        while count < step - 1:
            node = node.next
            count += 1
        new_head = node.next
        node.next = None
        return new_head
