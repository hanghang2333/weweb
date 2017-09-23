class Solution:
    def spiralOrder(self,matrix):
        ret = []
        while matrix:
            ret = ret + matrix[0]
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret = ret + matrix.pop(0)[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

a = Solution()
print(a.spiralOrder())
