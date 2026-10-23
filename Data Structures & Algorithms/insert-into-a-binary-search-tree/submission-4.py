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
            if not node.left and not node.right:
                if node.val > val:
                    node.left = insert
                else:
                    node.right = insert
                return
            elif not node.left:
                if node.val > val:
                    node.left = insert
                    return
                dfs(node.right)
            elif not node.right:
                if node.val < val:
                    node.right = insert
                    return
                dfs(node.left)
            else:
                if node.val > val:
                    dfs(node.left)
                else:
                    dfs(node.right)


        dfs(root)
        return root