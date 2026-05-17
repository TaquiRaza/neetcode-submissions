# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, a, b) -> bool:
        if a is None and b is None:
            return True
        
        if a is None or b is None:
            return False
        
        if a.val != b.val:
            return False
        
        if not self.isSameTree(a.left, b.left):
            return False
        
        if not self.isSameTree(a.right, b.right):
            return False
        
        return True
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        if root is None and subRoot is not None:
            return False

        if self.isSameTree(root, subRoot):
            return True
            
        if self.isSubtree(root.left, subRoot):
            return True
        
        if self.isSubtree(root.right, subRoot):
            return True
        
        return False