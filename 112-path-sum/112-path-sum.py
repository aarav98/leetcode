# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(node: Optional[TreeNode]):
            if node.left is None and node.right is None:
                return True
            return False
        
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, curr_sum = stack.pop()
            
            if isLeaf(node) and curr_sum == 0:
                return True
            
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
                
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
                
        return False
        
        
#         recursive
#         def isLeaf(node: Optional[TreeNode]):
#             if node.left is None and node.right is None:
#                 return True
#             return False
        
#         if not root:
#             return False
        
#         if isLeaf(root):
#             return root.val == targetSum
        
        
#         left = self.hasPathSum(root.left, targetSum-root.val)
#         right = self.hasPathSum(root.right, targetSum-root.val)
        
#         return left or right
        
                
            
                
                
                
        