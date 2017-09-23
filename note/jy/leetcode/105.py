class Solution(object):
    def diedai(self,pre,ino,inx):
        root = TreeNode(ino[inx[0]])
        medinx = pre.index(ino[inx[0]])
        tmpleft = pre[0:medinx]
        if len(tmpleft)>=1:
            inx[0] = inx[0]+1
            root.left = self.diedai(pre[0:medinx],ino,inx)
        else:
            root.left = None
        tmpright = pre[medinx+1:]
        if len(tmpright)>=1:
            inx[0] = inx[0]+1
            root.right = self.diedai(pre[medinx+1:],ino,inx)
        else:
            root.right = None
        return root
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        root = self.diedai(inorder,preorder,[0])
        return root
