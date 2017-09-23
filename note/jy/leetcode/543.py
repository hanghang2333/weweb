# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diedaidepth(self,root):
        res = 0
        if root==None:
            res = 0
        else:
            res = 1+max(self.diedaidepth(root.left),self.diedaidepth(root.left))
        return res
    def diedaipath(self,root,tmp):
        if root==None:
            return
        else:
            tmp.append(self.diedaidepth(root.left)+self.diedaidepth(root.right))
            self.diedaipath(root.left,tmp)
            self.diedaipath(root.right,tmp)
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.diedaipath(root,res)
        print(res)
        return max(res)
