# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root):
        if root==None:
            return (0,0)
        l = self.dd(root.left)
        r = self.dd(root.right)
        return (l[1]+r[1],max(l[1]+r[1],l[0]+r[0]+root.val))

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dd(root)[1]
