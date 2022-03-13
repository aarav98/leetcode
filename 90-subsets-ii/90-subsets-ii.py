class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        prev, curr = None, None
        nums = sorted(nums)
        prev_subsets = None
        
        for curr in nums:
            new_subsets = []
            iterate_over = None
            if prev == curr:
                iterate_over = prev_subsets
            else:
                iterate_over = subsets
            
            for subset in iterate_over:
                s = subset.copy()
                s.append(curr)
                new_subsets.append(s)
            
            subsets += new_subsets
            prev = curr
            prev_subsets = new_subsets
            
        return subsets
                
                
        