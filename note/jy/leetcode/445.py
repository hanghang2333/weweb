# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None or l2==None:
            return l1 if l1!=None else l2
        stack1 = []
        stack2 = []
        while l1!=None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2!=None:
            stack2.append(l2.val)
            l2 = l2.next
        nowout = 0
        res = []
        while len(stack1)+len(stack2)>0:
            n1 = 0
            n2 = 0
            if len(stack1)!=0:
                n1 = stack1.pop()
            if len(stack2)!=0:
                n2 = stack2.pop()
            r = (n1+n2+nowout)%10
            nowout = (n1+n2+nowout)/10
            res.append(r)
        if nowout!=0:
            res.append(nowout)
        print(res)
        head = ListNode(res[-1])
        ttt = head
        for i in range(-2,-1,-1):
            tmp = ListNode(res[i])
            head.next = tmp
            head = head.next
        return ttt
