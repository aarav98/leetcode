import bisect
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        idx = bisect.bisect_right(letters, target) % len(letters)
        return letters[idx]
            
            
        