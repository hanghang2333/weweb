# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValid(self,root,res):
        if root.left!=None:
            self.isValid(root.left,res)
        res.append(root.val)
        if root.right !=None:
            self.isValid(root.right,res)
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.isValid(root,res)
        minv = res[-1]-res[0]
        for i in range(len(res)-1):
            minv = min(minv,res[i+1]-res[i])
        return minv
