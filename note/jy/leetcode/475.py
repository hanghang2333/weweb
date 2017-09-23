class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        import bisect
        res = []
        if len(heaters)==1:
            return max([abs(i-heaters[0]) for i in houses])
        for i in houses:
            idx = bisect.bisect(heaters,i)
            print(heaters,i,idx)
            if idx==0:
                res.append(abs(heaters[0]-i))
            elif idx==len(heaters):
                res.append(abs(i-heaters[-1]))
            else:
                res.append(min(i-heaters[idx-1],heaters[idx]-i))
        print(res)
        return max(res)
a = Solution()
print(a.findRadius([1,1,1,1,1,1,999,999,999,999,999],[499,500,501]))
