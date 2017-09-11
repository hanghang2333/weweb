class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [2,3,-2,4]----[2,3]
        [1,2,3,-4,-5,6,7]
        """
        n = len(nums)
        imax = nums[0]
        imin = nums[0]
        r = nums[0]
        for i in range(1,n):
            if nums[i]<0:
                imax,imin = imin,imax
            imax = max(imax*nums[i],nums[i])
            imin = min(imin*nums[i],nums[i])
            r = max(r,imax)
        return r
