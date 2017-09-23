class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low,high = 0,0
        for i in range(len(s)):
            if s[i]=='(':
                low = low + 1
                high = high + 1
            elif s[i]==')':
                low = max(low - 1,0)
                high = high - 1
            else:
                low = max(0,low-1)
                high = high + 1
            if high<0:
                return False
        return low==0
    def ss(self,s):
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack = [i+1 for i in stack if i+1>=0]
            elif s[i]==')':
                stack = [i-1 for i in stack if i-1>=0]
            else:
                tmp = []
                for i in stack:
                    tmp.append(i)
                    tmp.append(i+1)
                    if i-1>=0:
                        tmp.append(i-1)
                stack = list(set(tmp))
        return min(stack)==0
