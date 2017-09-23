class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        def isvaild(x,y,m,n):
            if x>=0 and x<m and y>=0 and y<n:
                return True
            return False
        d = {'s':(-1,0),'z':(0,-1)}
        res = 0
        for row in range(m):
            for col in range(n):
                if board[row][col]=='X':
                    flag = True
                    for f in d:
                        newx = row+d[f][0]
                        newy = row+d[f][1]
                        if isvaild(newx,newy,m,n) and board[newx][newy]=='X':
                            flag = False
                            break
                    if flag:
                        res = res + 1
        return res
