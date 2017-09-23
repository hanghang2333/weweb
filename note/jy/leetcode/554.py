class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
        """
        if len(wall)==0:
            return 0
        res = []
        for row in wall:
            start = 0
            for i in range(len(row)-1):
                start = start + row[i]
                res.append(start)
        maxcount = 0
        d = {}
        for i in res:
            if i==0:
                continue
            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1
        for i in d:
            maxcount = max(maxcount,d[i])
        return len(wall)-maxcount
a = Solution()
r = [1 for i in range(100000)]
print a.leastBricks([[1]])
