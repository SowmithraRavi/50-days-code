class Solution:
    def InOrder(self,root, res=None):
        if res is None:
            res = []
        if root is not None:
            self.InOrder(root.left, res)
            res.append(root.data)
            self.InOrder(root.right, res)
        return res
