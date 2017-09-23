class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from copy import copy
        nums.sort()
        n = len(nums)
        if n==0:
            return []
        dp = [0]*n
        dp[0]= [nums[0]]
        for i in range(1,n):
            curNum = nums[i]
            maxSet = []
            for j in range(i):
                if curNum%nums[j]==0:
                    localSet = copy(dp[i])
                    if len(localSet)>len(maxSet):
                        maxSet = localSet
            maxSet.append(nums[i])
            dp[i] = maxSet
        res = []
        for localSet in dp:
            if len(localSet)>len(res):
                res = localSet
        return res

a = Solution()
print(a.largestDivisibleSubset([4,8,10,240]))
