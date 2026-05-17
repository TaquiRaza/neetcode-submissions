# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node) -> TreeNode:
            if not node:
                return None
            res = TreeNode(node.val)
            res.right = dfs(node.left)
            res.left = dfs(node.right)
            return res
        
        return dfs(root)