# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        
        if not root:
            return depth
        q.append(root)
        found = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if not node.left and not node.right:
                    found = True
                    break
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            depth += 1
            if found:
                break
                
        return depth
                
                