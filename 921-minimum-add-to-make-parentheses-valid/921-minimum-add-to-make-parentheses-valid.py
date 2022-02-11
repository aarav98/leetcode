class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        stack = []
        count = 0
        
        for curr_elem in s:
            if curr_elem == "(":
                stack.append(curr_elem)
            else:
                if stack:
                    stack.pop()
                else:
                    count+=1

                    
        return count + len(stack)