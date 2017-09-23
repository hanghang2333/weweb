class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix==[]:
            return []
        path = {'up':(-1,0),'down':(1,0),'left':(0,-1),'right':(0,1)}
        nx = len(matrix)
        ny = len(matrix[0])
        def getvalid(now,nx,ny):
            #print('now',now)
            res = []
            for i in path:
                x = now[0]+path[i][0]
                y = now[1]+path[i][1]
                if x>=0 and x<=nx-1 and y>=0 and y<=ny-1:
                    res.append((x,y))
            return res
        def getallvalid(nowlist):
            #print('nowlist',nowlist)
            res = []
            for i in nowlist:
                tmp = getvalid(i,nx,ny)
                res = res + tmp
            res = list(set(res))
            return res
        def has0(res):
            #print('res',res)
            flag = False
            for i in range(len(res)):
                if matrix[res[i][0]][res[i][1]] == 0:
                    return True
            return False
        result = [[0 for i in range(ny)]for j in range(nx)]
        def dfs(now,depth):
            res = getallvalid(now)
            if has0(res):
                return depth
            else:
                return dfs(res,depth+1)
        for i in range(nx):
            for j in range(ny):
                if matrix[i][j]==0:
                    result[i][j]=0
                else:
                    result[i][j]=dfs([[i,j]],1)
        return result

a = Solution()
d=[[0,0,0],[0,1,0],[1,1,1]]
e=[[0],[0],[1],[0]]
print(a.updateMatrix(e))
