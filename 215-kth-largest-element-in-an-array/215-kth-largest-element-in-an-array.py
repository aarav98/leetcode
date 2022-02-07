class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            # store pointer is always lagging behind i
            # and points to a value that is >= pivot
            # so we swap whenever we see a smaller element at index i
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def quickselect(left, right, k_smallest):
            """
            returns kth smallest element of the list within left...right
            """
            
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left,right) # both left, right included
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return quickselect(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return quickselect(0, len(nums) - 1, len(nums) - k)
                
                
            
        