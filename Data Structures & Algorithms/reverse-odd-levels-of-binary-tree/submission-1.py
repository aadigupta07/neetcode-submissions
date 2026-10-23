# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = -1

        queue = deque([root])

        # will do one pass to get the values in a list, reverse the list, then do another pass to assign values by index


        while queue:
            depth+=1
            result = []
            if depth % 2 == 1:
                for i in range(len(queue)):
                    curr = queue[i]
                    result.append(curr.val)
                
                result = result[::-1]

                for i in range(len(queue)):
                    curr = queue.popleft()
                    curr.val = result[i]
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            
            else:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        
        return root
                
                
            
                
                
                


                

