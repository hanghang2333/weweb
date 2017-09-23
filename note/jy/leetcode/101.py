# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sifftwo(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1!=None and root2==None or root1==None and root2!=None:
            return False
        if root1.val!=root2.val:
            return False
        return self.sifftwo(root1.left,root2.right) and self.sifftwo(root1.right,root2.left)
    def iorder(self,root,res):
        if root == None:
            return
        elif root.left!=None and root.right==None:
            self.iorder(root.left,res)
            res.append(root.val)
            res.append('null')
        elif root.left==None and root.right!=None:
            res.append('null')
            res.append(root.val)
            self.iorder(root.right,res)
        else:
            self.iorder(root.left,res)
            res.append(root.val)
            self.iorder(root.right,res)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        res = []
        self.iorder(root,res)
        print(res)
        for i in range(len(res)):
            if res[i]!=res[len(res)-i-1]:
                return False
        return True
        '''
        return self.sifftwo(root.left,root.right)
