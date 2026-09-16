# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowest = None

        def dfs(root, p, q):
            if not root:
                return
            if root.val >= min(p.val, q.val) and root.val <= max(p.val, q.val):
                self.lowest = root
                return
            if root.val <= min(p.val, q.val):
                dfs(root.right, p, q)
            else:
                dfs(root.left, p, q)
            

            
        dfs(root, p, q)

        return self.lowest