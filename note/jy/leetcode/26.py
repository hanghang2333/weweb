class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = nums[0]
        n = len(nums)
        top = nums[0]
        topinx = 1
        for i in range(1,n):
            if nums[i]!=top:
                nums[topinx] = nums[i]
                top = nums[topinx]
                topinx = topinx + 1
        print(nums)
        return topinx
a = Solution()
print(a.removeDuplicates([1,2,3,3,4,4,4,5,5,6]))
