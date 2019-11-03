# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        prob_a = headA
        prob_b = headB

        while prob_a != prob_b:
            prob_a = prob_a.next if prob_a is not None else headB
            prob_b = prob_b.next if prob_b is not None else headA
        return prob_a
