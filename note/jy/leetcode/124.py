# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dd(self,root):
        if root.left==None and root.right==None:
            return root.val,root.val
        if root.left==None:
            r = self.dd(root.right)
            return max(root.val+r[1],r[0],root.val),max(root.val,r[1]+root.val,root.val)
        if root.right==None:
            r = self.dd(root.left)
            return max(root.val+r[1],r[0],root.val),max(root.val,r[1]+root.val,root.val)
        if root.left!=None and root.right!=None:
            l = self.dd(root.left)#f2,f1,l,r--f2 not root
            r = self.dd(root.right)
            return max(root.val+l[1],root.val+r[1],root.val+l[1]+r[1],max(l[0],r[0]),root.val),max(l[1]+root.val,r[1]+root.val,root.val)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = self.dd(root)
        print(d)
        return max(d)
