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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        maxnow = 0
        self.isValid(root,res)
        n = len(res)
        if n == 1:
            return res
        i = 0
        rrr = []
        while i<n:
            time = 1
            while i+1<n and res[i]==res[i+1]:
                i = i + 1
                time = time + 1
            if time > maxnow:
                rrr = []
                rrr.append(res[i])
                maxnow = time
            elif time == maxnow:
                rrr.append(res[i])
            i = i + 1
        return rrr
a = Solution()
