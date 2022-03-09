"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        q = deque()
        q.append(root)
        
        while q:
            popped = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                popped += 1
                if popped < n:
                    node.next = q[0]
                    
                if node.left:    
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return root

            
        
        
        