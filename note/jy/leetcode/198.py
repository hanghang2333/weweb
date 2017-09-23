class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums) ==1:
            return nums[0]
        maxv = 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2,len(nums)):
            dp[i] = max(max(dp[0:i-1])+nums[i],nums[i])
        #print(dp)
        return max(dp)
a = Solution()
a.rob([2,1,1,2])
