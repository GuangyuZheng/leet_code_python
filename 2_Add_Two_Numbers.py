# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = l1.val + l2.val
        if num >= 10:
            head = ListNode(num - 10)
            carry = 1
        else:
            head = ListNode(num)
            carry = 0

        tmp_node = head
        while True:
            if carry == 0 and l1.next is None and l2.next is None:
                break
            else:
                num = l1.next.val if l1.next else 0
                num += l2.next.val if l2.next else 0
                num += carry
                if num >= 10:
                    tmp_node.next = ListNode(num - 10)
                    carry = 1
                else:
                    tmp_node.next = ListNode(num)
                    carry = 0
            tmp_node = tmp_node.next
            l1 = l1.next if l1.next is not None else l1
            l2 = l2.next if l2.next is not None else l2
        return head
