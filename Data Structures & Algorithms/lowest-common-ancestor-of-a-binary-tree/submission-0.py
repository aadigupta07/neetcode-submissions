# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        self.deepest = -1
        
        def inTree(root, node):
            if not root:
                return
            if root == node:
                return True
            return inTree(root.left, node) or inTree(root.right, node)


        def dfs(root, depth):
            if not root:
                return
            if inTree(root, p) and inTree(root, q) and depth > self.deepest:
                self.deepest = depth
                self.result = root
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
            
        dfs(root, 0)
        return self.result






