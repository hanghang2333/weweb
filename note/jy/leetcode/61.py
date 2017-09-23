# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        count = 0
        headbak = head
        while(head!=None):
            head = head.next
            count = count + 1
        k = k%count
        inx = count - k
        prehead = ListNode(0)
        prehead.next = headbak
        preheadbak = ''
        for i in range(count):
            print(i,headbak.val,prehead.next)
            if i==inx:
                preheadbak = headbak
            if i == count -1:
                headbak.next = prehead.next
            headbak = headbak.next
        headbak = prehead.next
        for i in range(count):
            if i==inx-1:
                headbak.next = None
                break
            else:
                headbak = headbak.next
        return preheadbak
