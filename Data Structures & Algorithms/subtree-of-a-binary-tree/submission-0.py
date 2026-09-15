# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(node1, node2):
            if not node1 or not node2:
                return node1 == node2
            if node1.val != node2.val:
                return False
            
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        def dfs(root, subRoot):
            if not root or not subRoot:
                return False
            
            if root.val == subRoot.val:
                return isSameTree(root, subRoot)
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
            
        
        
            
            