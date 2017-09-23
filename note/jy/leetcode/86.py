# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        root1 = ListNode(0)
        root1bak = root1
        root2 = ListNode(0)
        root2bak = root2
        mid = ''
        while head!=None:
            if head.val<x:
                root1.next = head
                root1 = root1.next
            elif head.val>=x:
                root2.next =head
                root2 = root2.next
            head = head.next
        root1.next = root2bak.next
        return root1bak.next
