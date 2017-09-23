class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        stack1 = [int(i) for i in num1]
        stack2 = [int(i) for i in num2]
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
        res.reverse()
        res = [str(i) for i in res]
        r = ''.join(res)
        return r
