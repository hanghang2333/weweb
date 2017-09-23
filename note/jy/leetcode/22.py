class Solution(object):
    def dd(self,res,restmp,alllen,nowlen,q):
        #print(alllen,nowlen,q)
        if nowlen == alllen and q==0:
            res.append(restmp)
            return
        if nowlen>=alllen:
            return
        for i in {'(',')'}:
            if q==0 and i ==')':
                continue
            else:
                restmpbak = restmp+i
                if i=='(':
                    self.dd(res,restmpbak,alllen,nowlen+1,q+1)
                else:
                    self.dd(res,restmpbak,alllen,nowlen+1,q-1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        restmp = ''
        alllen = n*2
        self.dd(res,restmp,alllen,0,0)
        #print(res)
        return res
a = Solution()
print(a.generateParenthesis(0))
