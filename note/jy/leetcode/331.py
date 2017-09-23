class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        top = -1
        preorder = preorder.split(',')
        for i in preorder:
            stack.append(i)
            top = top+1
            while(self.endtwox(stack)):
                stack.pop()
                top = top -1
                stack.pop()
                top = top -1
                if top<0:
                    return False
                stack.pop()
                stack.append('#')
                top = top + 1
        if len(stack)==1:
            if stack[0]=='#':
                return True
        return False
    def endtwox(self,stack):
        if len(stack)<=1:
            return False
        if stack[-1]=='#' and stack[-2]=='#':
            return True
