# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        insert = TreeNode(val)
        if not root:
            return insert
        
        def dfs(node):
            if node.val > val:
                if not node.left:
                    node.left = insert
                    return
                dfs(node.left)
            if node.val < val:
                if not node.right:
                    node.right = insert
                    return
                dfs(node.right)
            


        dfs(root)
        return root