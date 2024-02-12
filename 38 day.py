class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if root==None:
            return 0
        else:
            l=self.height(root.left)
            r=self.height(root.right)
            return max(l,r)+1
