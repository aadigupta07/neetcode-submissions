# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # watch out for medium.left = small and small.right = large
        self.is_valid = True
        def dfs(node, lower, higher):
            if not node:
                return
            if node.left and node.left.val > lower:
                self.is_valid = False
                return
            if node.right and node.right.val < higher:
                self.is_valid = False
                return
            if node.left and node.left.val < lower:
                lower = node.left.val
            if node.right and node.right.val > higher:
                higher = node.right.val
            
            dfs(node.left, lower, higher)
            dfs(node.right, lower, higher)
                
        
        dfs(root, root.val, root.val)
        return self.is_valid
            
            

            
            