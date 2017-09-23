class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k == 0:
            dou = []
            d = {}
            for i in nums:
                if i in d:
                    d[i] = d[i] + 1
                else:
                    d[i] = 1
            for i in d:
                if d[i]>1:
                    res = res + 1
            return res
        else:
            nums = set(nums)
            d = {}
            for i in nums:
                d[i] =1
            if k<0:
                return 0
            for i in nums:
                if k+i in d:
                    res = res + 1
        return res
a = Solution()
print a.findPairs([1,1,1,2,3,4,5],1)
