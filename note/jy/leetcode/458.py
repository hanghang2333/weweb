class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        res = 1.0*math.log(buckets)/math.log(minutesToTest/minutesToDie+1)
        if int(res)==res:
            return int(res)
        else:
            return int(res)+1
