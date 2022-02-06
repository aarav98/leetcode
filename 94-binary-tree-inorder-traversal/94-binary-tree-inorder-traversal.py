# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        rootToProcess = root
        while rootToProcess or stack:
            while rootToProcess:
                stack.append(rootToProcess)
                rootToProcess = rootToProcess.left
            curr = stack.pop()
            result.append(curr.val)
            rootToProcess = curr.right
        
        return result