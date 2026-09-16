# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowest = None

        def containsNode(root, node):
            if not root:
                return False
            if root == node:
                return True
            return containsNode(root.left, node) or containsNode(root.right, node)

            
        def dfs(node, p, q):
            if not node:
                return
            if containsNode(node, p) and containsNode(node, q):
                self.lowest = node
            dfs(node.left, p, q)
            dfs(node.right, p, q)
        
        dfs(root, p, q)
            
            

        return self.lowest