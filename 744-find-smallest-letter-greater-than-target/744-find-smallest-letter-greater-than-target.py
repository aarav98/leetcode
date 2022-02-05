"""
1 2 3   4   5   5   6 7

0 1 2   3   4   5   6 7
"""

import bisect
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        left, right = 0, len(letters)
        
        while left < right:
            mid = left + (right-left)//2
            
            if letters[mid] > target:
                right = mid
            else:
                left = mid+1
        
        return letters[left%len(letters)]
            
            
        # idx = bisect.bisect_right(letters, target) % len(letters)
        # return letters[idx]
            
            
        