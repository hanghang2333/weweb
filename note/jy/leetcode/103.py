# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root,d,depth):
        if root==None:
            return
        if depth in d:
            d[depth].append(root.val)
        else:
            d[depth]=[root.val]
        self.dd(root.left,d,depth+1)
        self.dd(root.right,d,depth+1)
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        self.dd(root,d,0)
        res = []
        for i in range(len(d)):
            if i%2==1:
                tmp = d[i]
                tmp.reverse()
                res.append(tmp)
            else:
                res.append(d[i])
        return res

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
