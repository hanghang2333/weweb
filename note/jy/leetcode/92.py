# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def rever(head,length):#length = n-m+1=3
            prehead = ListNode(0)
            prehead.next = head
            for i in range(length-1):
                nextone = head.next
                #nextonenext = nextone.next
                nextone.next = head
                head = nextone
            return head,prehead.next
        prehead = ListNode(0)
        prehead.next = head
        headbak = head
        while m-2!=0:
            headbak = headbak.next
        hheadbak = headbak
        headbak = head
        while n-1!=0:
            headbak = headbak.next
        taibak = headbak.next
        n1,n2 = rever(hheadbak.next,n-m+1)
        hheadbak.next = n1
        n2.next = taibak
        return prehead.next
