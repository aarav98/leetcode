class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        seen = set()
        last_occurence = {c:i for i,c in enumerate(s)}
        
        for i,c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurence[stack[-1]]:
                    seen.discard(stack.pop())
                
                seen.add(c)
                stack.append(c)
        return "".join(stack)
        