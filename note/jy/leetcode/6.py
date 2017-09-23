class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows==1 or len(s)<=numRows:
            return s
        numyizu = numRows+numRows-2
        numrjy = numRows-1
        n = len(s)
        numzu = n/numyizu
        res = [[False for i in range((numzu+1)*numrjy)] for j in range(numRows)]
        for i in xrange(n):
            nowzu = i/numyizu
            nowzunei = i%numyizu
            startlie = nowzu*numrjy
            nowlie = startlie
            nowhang = nowzunei
            if nowzunei>=numRows:
                nowlie = startlie+(nowzunei+1-numRows)
                nowhang = numrjy*2-nowzunei
            res[nowhang][nowlie] = s[i]
        result = []
        #return ''.join(''.join(i) for i in res)
        for hang,i in enumerate(res):
            tup = (numrjy,numrjy)
            if hang!=0 and hang!=numrjy:
                tup = (numrjy-hang,hang)
            inx = 0
            nowj = inx
            result.append(i[nowj])
            #print(tup)
            nowj = nowj+tup[inx]
            while nowj<(numzu+1)*numrjy:
                #nowj = nowj+tup[inx]
                inx = 0 if inx==1 else 1
                #if nowj<(numzu+1)*(numRows-1):
                    #print(hang,nowj)
                if i[nowj] != False:
                    result.append(i[nowj])
                nowj = nowj+tup[inx]
        return ''.join(result)


a = Solution()
#print(a.convert("twckwuyvbihajbmhmodminftgpdcbquupwflqfiunpuwtigfwjtgzzcfofjpydjnzqysvgmiyifrrlwpwpyvqadefmvfshsrxsltbxbziiqbvosufqpwsucyjyfbhauesgzvfdwnloojejdkzugsrksakzbrzxwudxpjaoyocpxhycrxwzrpllpwlsnkqlevjwejkfxmuwvsyopxpjmbuexfwksoywkhsqqevqtpoohpd",4))
print(a.convert('PAYPALISHIRING',3))
