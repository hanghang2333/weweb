class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = len(nums)-1
        rem = 0
        i = 0
        while i<len(nums)-rem:
            if nums[i]==val:
                nums[i]=nums[end]
                end = end -1
                rem = rem + 1
            else:
                i = i + 1
        return len(nums)-rem

        
