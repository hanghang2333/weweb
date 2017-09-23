# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nn = 0
        headbak = head
        while headbak!=None:
            nn = nn + 1
            headbak = headbak.next
        nns = 0
        if nn==n:
            return head.next
        headbak = head
        while headbak!=None and nns<nn-n-1:
            nns = nns + 1
            headbak = headbak.next
        tmp = headbak.next.next
        headbak.next = tmp
        return head
