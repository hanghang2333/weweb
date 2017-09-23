# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self,root):
        return -1 if root==None else 1+self.height(root.left)
    def countNodes(self,root):
        h = self.height(root)
        return 0 if h<0 else (1<<h)+self.countNodes(root.right) if self.height(root.right)==h-1 else (1<<h-1)+self.countNodes(root.left)


        
