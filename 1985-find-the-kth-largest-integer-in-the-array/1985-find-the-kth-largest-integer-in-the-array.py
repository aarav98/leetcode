import random
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            
            i, j = 0, 0
            k = right
            
            while j <=k:
                if int(nums[j]) < int(pivot):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif int(nums[j]) >  int(pivot):
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
                else:
                    j += 1
            
            return i, j
        
        def quickselect(left, right, k_smallest):
            
            if left==right:
                return nums[left]
            
            pivot_index = random.randint(left,right)
            pi_start, pi_end = partition(left, right, pivot_index)
            
            if k_smallest >=pi_start and k_smallest < pi_end:
                return nums[pi_start]
            elif k_smallest < pi_start:
                return quickselect(left, pi_start-1, k_smallest)
            else:
                return quickselect(pi_end, right, k_smallest)
        
        return quickselect(0, len(nums)-1, len(nums)-k)

            
        