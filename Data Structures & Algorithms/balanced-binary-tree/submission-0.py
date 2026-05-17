# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return True, 0
            
            leftB, leftH = dfs(node.left)
            rightB, rightH = dfs(node.right)
            
            h = 1 + max(leftH, rightH)

            if not leftB or not rightB:
                return False, h
            
            return abs(leftH - rightH) < 2, h
        
        return dfs(root)[0]