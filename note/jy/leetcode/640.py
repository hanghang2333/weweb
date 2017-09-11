class Solution(object):
    def makexp(self,str):
        xcount = 0
        numcount = 0
        start = 0
        end = 0
        i = 0
        while i < len(str):
            if str[i]=='+' or str[i]=='-':
                start = i
                i = i + 1
            while i<len(str) and (str[i]!='+' and str[i]!='-') :
                i = i + 1
            end = i
            tmp = str[start:end]
            if 'x' in tmp:
                xcount = xcount + int(tmp[0:-1])
            else:
                numcount = numcount + int(tmp)
            if end==len(str)-1:
                break
        return xcount,numcount
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        str1 = equation[0:equation.index('=')]
        str2 = equation[equation.index('=')+1:]
        if str1[0]!='-':
            str1 = '+'+str1
        if str2[0]!='-':
            str2 = '+'+str2
        str1 = str1.replace('+x','+1x')
        str1 = str1.replace('-x','-1x')
        str2 = str2.replace('+x','+1x')
        str2 = str2.replace('-x','-1x')
        x1,n1 = self.makexp(str1)
        x2,n2 = self.makexp(str2)
        x = x1-x2
        n = n1-n2
        result = ''
        if x==0 and n!=0:
            result = 'No solution'
        elif x==0 and n == 0:
            result = 'Infinite solutions'
        else:
            result = 'x='+str(-1*n/x)
        return result
a=Solution()
print a.solveEquation('x+5-3+x=6+x-2')
