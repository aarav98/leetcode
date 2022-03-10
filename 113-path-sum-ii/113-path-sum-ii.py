# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        stack = [(root, targetSum - root.val, [root.val])]
        result = []
        
        while stack:
            node, sum, ls = stack.pop()
            
            if not node.left and not node.right and sum == 0:
                result.append(ls)
            
            if node.right:
                stack.append((node.right, sum-node.right.val, ls+[node.right.val]))
            
            if node.left:
                stack.append((node.left, sum-node.left.val, ls+[node.left.val]))
        
        return result
        
            