class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return [0,0]
        if len(nums)==1:
            return [nums[0],0]
        res = nums[0]
        for i in range(1,len(nums)):
            res = res^nums[i]
        s = bin(res)
        if '1' not in s:
            return [0,0]
        r = res&~(res-1)
        num1 = 0
        num2 = 0
        for i in nums:
            if  i&r>0:
                num1 = num1^i
            else:
                num2 = num2^i
        return [num1,num2]
        '''
        r1 = nums[0]
        nr = r1&r
        print(r,r1,nr)
        for i in range(1,len(nums)):
            if nums[i]&r==nr:
                r1 = r1^nums[i]
        r2 = res^r1
        return [r1,r2]
        '''
a = Solution()
print(a.singleNumber([43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]))
