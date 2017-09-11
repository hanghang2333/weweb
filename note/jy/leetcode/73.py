class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        lx = len(matrix)
        ly = len(matrix[0])
        d = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    d.add((row,col))
        for (i,j) in d:
            nowx = i
            nowy = j
            print(i,j)
            matrix[i]=[0 for k in range(ly)]
            for k in range(lx):
                matrix[k][j]=0
        return matrix
a = Solution()
print a.setZeroes([[1,2,3],[0,1,1],[1,1,1]])
