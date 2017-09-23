# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headAbak = headA
        headBbak = headB
        while headAbak.next!=None:
            headAbak = headAbak.next
        headAbak.next = headBbak
        slow = headA
        fast = headA
        hashuan = False
        while fast.next.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                hashuan = True
                break
        if hashuan==False:
            return None
        nowheadA = headA
        while nowheadA!=slow:
            nowheadA = nowheadA.next
            slow = slow.next
        headAbak.next = None
        return nowheadA
