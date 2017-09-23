class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        if x<=3:
            return 1
        low = 1
        high = int(x/2)
        while low<high:
            print('s',low,high)
            mid = int((low+high)/2)
            if mid*mid==x:
                return mid
            if mid*mid<x:
                low = mid+1
            else:
                high = mid -1
            print('e',low,high)
        if high*high>x:
            return low
        return high

a = Solution()
print(a.mySqrt(123))
