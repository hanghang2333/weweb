# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        d1 = {}
        d2 = {}
        newhead = ListNode(0)
        newheadbak = newhead
        headbak = head
        idx = 1
        while head!=None:
            tmp = ListNode(head.val)
            newhead.next = tmp
            d[idx] = tmp
            d1[head] = idx
            head = head.next
            newhead = newhead.next
            idx = idx + 1
        
