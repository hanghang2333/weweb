class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {1:'*',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz',0:' '}
        n = len(digits)
        if n == 0:
            return []
        res = list(d[int(digits[0])])
        if n == 1:
            return res
        for i in digits[1:]:#2
            now = d[int(i)]#abc
            tmp = []
            for j in now:#a
                for k in res:
                    tmp.append(k+j)
            res = tmp
        return res
a = Solution()
print(a.letterCombinations('232'))
