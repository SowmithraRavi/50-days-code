class Solution:
    
    def topView(self,root):
        if not root:
            return []
        queue = [(root, 0)]
        topview = {}
        
        while queue:
            node, hd = queue.pop(0) 
            if hd not in top_view:
                topview[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        sortview = [topview[hd] for hd in sorted(topview.keys())]
        return sortview
