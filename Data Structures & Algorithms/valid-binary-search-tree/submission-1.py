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
            if node.val < lower or node.val > higher:
                self.is_valid = False
                return
            
            dfs(node.left, lower, node.val)
            dfs(node.right, node.val, higher)
                
        
        dfs(root, float('-inf'), float('inf'))
        return self.is_valid
            
            

            
            