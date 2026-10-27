# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs_sum(node, total):
            if not node:
                return 0
            left = 0
            right = 0
            if node.left:
                left = dfs_sum(node.left, total+node.val)
            if node.right:
                right = dfs_sum(node.right, total + node.val)
            total += max(left, right)
            return total
            
        self.best = 0
        def dfs(node):
            if not node:
                return
            self.best = max(self.best, dfs_sum(node.right, node.val) + dfs_sum(node.left, node.val))
            dfs(node.left)
            dfs(node.right)
            
        
        dfs(root)
        return self.best
        
        