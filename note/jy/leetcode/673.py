class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        res = [1 for _ in range(n+1)]
        for i in range(2,n+1):
            tmp = 0
            for k in range(1,i):
                if nums[i-1-k]<nums[i-1]:
                    tmp = max(dp[i-k],tmp)
            #bj = [dp[i-k] for k in range(1,i) if nums[i-1-k]<nums[i-1]]
            #tmp = 0 if len(bj)==0 else max(bj)
            #print(tmp,bj,i,nums)
            here = 0
            for k in range(1,i):
                if nums[i-1-k]<nums[i-1] and dp[i-k]==tmp:
                    here = here + res[i-k]
            #here = sum([res[i-k] for k in range(1,i) if (nums[i-1-k]<nums[i-1] and dp[i-k]==tmp)])
            dp[i] = tmp+1
            res[i] = here if here>1 else 1
        dp = dp[1:]
        res = res[1:]
        #print(dp)
        #print(res)
        maxl = max(dp)
        r = 0
        for idx,i in enumerate(dp):
            if dp[idx]==maxl:
                r = r + res[idx]
        return r

a = Solution()
print(a.findNumberOfLIS([1,2,4,3,5,4,7,2]))
