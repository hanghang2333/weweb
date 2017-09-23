# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lr(self,idx,L,R):
        if idx<L:
            return 0
        if idx>R:
            return 2
        return 1
    def dd(self,root,L,R):
        if root==None:
            return None
        if self.lr(root.val,L,R)==0:
            return self.dd(root.right,L,R)
        elif self.lr(root.val,L,R)==2:
            return self.dd(root.left,L,R)
        else:
            root.left = self.dd(root.left,L,R)
            root.right = self.dd(root.right,L,R)
        return root

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        root = self.dd(root,L,R)
        return root
