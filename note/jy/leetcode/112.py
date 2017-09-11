# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root,res):
        if root.left!=None:
            root.left.val = root.left.val+root.val
            self.dd(root.left)
        if root.right!=None:
            root.right.val = root.right.val+root.val
            self.dd(root.right)
        if root.left == None and root.right==None:
            res.append(root.val)


    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        res = []
        self.dd(root,res)
        if sum in res:
            return True
        return False
