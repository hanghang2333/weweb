# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root,res,nowstr):
        if root==None:
            return
        nowstr = nowstr+'->'+root.val
        if root.left!=None:
            self.dd(root.left,resnowstr)
        if root.right!=None:
            self.dd(root.right,res,nowstr)
        if root.left==None and root.right==None:
            res.append(nowstr)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dd(root,res,'')
        print(res)
        return res
