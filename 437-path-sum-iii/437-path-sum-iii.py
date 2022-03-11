# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

[10,5,3,3]
[0,10,15,18,21] - prefix sum
[0,10,7,18]

[10,15,18,21]
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def countTargetSum(path):
            count = 0
            for i in range(len(ls)-1):
                if ls[-1] - ls[i] == targetSum:
                    count+=1
            return count
        
        if not root:
            return 0
        
        paths = 0
        stack = [(root, [0,root.val])]
        
        while stack:
            node, ls = stack.pop()
            
            
            paths += countTargetSum(ls)
            
            if node.left:
                stack.append((node.left, ls+[ls[-1]+node.left.val]))
            
            if node.right:
                stack.append((node.right, ls+[ls[-1]+node.right.val]))
        
        return paths
        