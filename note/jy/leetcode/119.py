class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #Solution 1
        '''
        res = [1]
        for i in range(rowIndex):
            res = [x+y for x,y in zip([0]+res,res+[0])]
        return res
        '''
        #Solution 2
        res = [1]
        for i in range(rowIndex):
            res1 = [0]+res+[0]
            res = [res1[i]+res1[i+1] for i in range(len(res1)-1)]
        return res
