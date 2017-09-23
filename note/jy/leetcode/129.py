# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root,res):
        if root==None:
            return
        if root.left==None and root.right==None:
            res.append(root.val)
            return
        if root.left!=None:
            root.left.val = root.val*10+root.left.val
            self.dd(root.left,res)
        if root.right!=None:
            root.right.val = root.val*10+root.right.val
            self.dd(root.right,res)
    def dd1(self,root,nowd,res):
        if root==None:
            res.append(nowd)
            return
        if root.left==None and root.right==None:
            res.append(nowd)
            return
        if root.left!=None:
            self.dd1(root.left,nowd+1,res)
        if root.right!=None:
            self.dd1(root.right,nowd+1,res)
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = []
        self.dd1(root,0,res)
        return min(res)


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.dd(root,res)
        print(res)
        return sum(res)
