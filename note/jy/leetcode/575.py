class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count = len(candies)
        cset = set(candies)
        return min(len(cset),count/2)
a = Solution()
print(a.distributeCandies([1,1,2,2,3,3,5,6]))
