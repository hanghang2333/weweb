# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        prehead = ListNode(0)
        prehead.next = head
        first = True
        bak = head
        while head!=None and head.next !=None:
            nextone = head.next
            head.next = nextone.next
            nextone.next = head
            prehead.next = nextone
            prehead = head
            head = head.next
            if first:
                bak = nextone
                first = False
        return bak
