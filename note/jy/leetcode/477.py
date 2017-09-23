class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            tmp0 = 0
            tmp1 = 0
            for j in range(len(nums)):
                if nums[j]%2==0:
                    tmp0 = tmp0+1
                else:
                    tmp1 = tmp1 + 1
                nums[j] = nums[j]/2
            res = res + tmp1*tmp0
        return res
a = Solution()
print(a.totalHammingDistance([4,14,2]))
