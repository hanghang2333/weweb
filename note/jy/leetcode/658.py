class Solution(object):
    def bs(self,nums,k):
        left = 0
        right = len(nums)-1
        if left>=right:
            return
        while left<=right:
            mid = (left+right)/2
            if nums[mid]==k:
                return mid
            elif nums[mid]<k:
                left = mid+1
            else:
                right = mid-1
        return mid
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = right = bisect.bisect_left(arr, x)
        while right - left < k:
            if left == 0: return arr[:k]
            if right == len(arr): return arr[-k:]
            if x - arr[left - 1] <= arr[right] - x: left -= 1
            else: right += 1
        return arr[left:right]
a = Solution()
print(a.bs([1,2,3,4,5,6,7],8))
