# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def calculateHeight(self,node):
        if not node:
            return 0
        left = self.calculateHeight(node.left)
        right = self.calculateHeight(node.right)
        
        
        self.diameter = max(left+right, self.diameter)
        
        return max(left,right)+1
        
        
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateHeight(root)
        return self.diameter
    
        
        
       
            