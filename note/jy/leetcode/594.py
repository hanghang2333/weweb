class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        numset = set(nums)
        numss = sorted(numset)
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1
        maxr = 0
        print(d,numss)
        for i in range(1,len(numss)):
            if numss[i]-numss[i-1]<=1:
                maxr = max(maxr,d[numss[i]]+d[numss[i-1]])
        return maxr
a = Solution()
print a.findLHS([0,0,0,0])
