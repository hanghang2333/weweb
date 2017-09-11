class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        "LRUD"
        origin = (0,0)
        for i in moves:
            if i=='L':
                origin[1] = origin[1]-1
            if i=='R':
                origin[1]=origin[1]+1
            if i=='U':
                origin[0]=origin[0]-1
            if i=='D':
                origin[0]=origin[0]+1
        if origin[0] == 0 and origin[1]==0:
            return True
        return False
