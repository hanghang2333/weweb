class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        shuziset = {'1','2','3','4','5','6','7','8','9','0'}
        n = len(s)
        stack = []
        start = 0
        while start<len(s) and s[start] in shuziset:
            start = start + 1
        if s[0] in shuziset:
            start = max(start,1)
            stack.append(int(s[0:start]))
        else:
            start = max(start,1)
            stack.append(s[0:start])
        idx = 1
        def zenjia(nowshuzi,s):
            if len(stack)==0:
                stack.append(nowshuzi)
                return
            if s:
                if stack[-1] in {'+','-'}:
                    fuhao = stack.pop()
                    shuzi = stack.pop()
                    res = 0
                    if fuhao=='+':
                        res = shuzi+nowshuzi
                    else:
                        res = shuzi-nowshuzi
                    zenjia(res,True)
                else:
                    print('e',stack)
                    stack.append(nowshuzi)
            elif nowshuzi in {'+','-','('}:
                stack.append(nowshuzi)
            else:
                value = stack.pop()
                stack.pop()
                zenjia(value,True)
        while len(stack)!=0 and idx<len(s):
            print(idx,stack)
            if s[idx] in shuziset:
                start = idx
                end = start
                while idx<len(s) and s[idx] in shuziset:
                    idx = idx + 1
                idx = max(idx,start+1)
                nowshuzi = int(s[start:idx])
                print('w',idx,'g',nowshuzi)
                zenjia(nowshuzi,True)
            else:
                zenjia(s[idx],False)
                idx = idx + 1
        return stack[0]

a = Solution()
print(a.calculate("0"))
