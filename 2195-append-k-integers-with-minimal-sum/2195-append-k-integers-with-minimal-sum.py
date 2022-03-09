
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        result = (k*(k+1))//2
        for num in sorted(set(nums)):
            if num<=k:
                result -= num
                k += 1
                result += k
                
        return result
    
    """
    After many tries figured out that cycle sort wasn't written correctly (< and <= issue) or range(1, len(nums) + 1) issue
    
    
    Getting TLE because have to iterate over k and k is very large, so another approach is needed
    """


            
#     def cycleSort(self, nums):
#         # put all elements in right index
#         i = 0
#         while(i < len(nums)):
#             j  = nums[i]-1
#             if  nums[i] in range(1,len(nums)+1) and nums[i] != nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#             else:
#                 i += 1
#         return 
            
#     def minimalKSum(self, nums: List[int], k: int) -> int:
#         self.cycleSort(nums) # O(n)
        
#         n = len(nums)
        
#         missing_numbers = []
#         extra_numbers = set()
        
#         for i in range(n):
#             if len(missing_numbers) < k:
#                 if nums[i] != i+1:
#                     missing_numbers.append(i+1)
#                     extra_numbers.add(nums[i])
#         i = 1
#         while len(missing_numbers) < k:
#             candidate_number = i+n
#             if candidate_number not in extra_numbers:
#                 missing_numbers.append(candidate_number)
#             i += 1
#         return sum(missing_numbers)



            
        
                
        