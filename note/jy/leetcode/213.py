class Solution(object):
    def rob1(self,nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0 for i in range(len(nums)+1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            print(i,dp)
            dp[i] = nums[i-1]+max([dp[k] for k in range(0,i-1)])
        print(dp)
        return max(dp)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        return max(self.rob1(nums[1:]),self.rob1(nums[0:-1]))

a = Solution()
print(a.rob([10,4,5,1,7,8]))
