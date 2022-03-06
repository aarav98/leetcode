class Solution {
//     public int firstMissingPositive(int[] nums) {
//         int n = nums.length;

//         boolean containsOne = false;
//         for(int i: nums){
//             containsOne = i==1;
//             break;
//         }
//         if (!containsOne) return 1;

//         for(int i=0 ; i<n; i++){
//             if (nums[i] < 1 || nums[i] > n) nums[i] = 1;
//         }

//         for(int i=0 ; i<n; i++){
//             if (nums[i] < 1 || nums[i] > n) nums[i] = 1;
//         }
        
//         for(int i = 0; i< n; i++){
//             int j = nums[i];
//             if(nums[j] < 1) continue;
//             nums[j] = -1*nums[j];
//         }
        
//         for(int i =1; i<n;i++){
//             if(nums[i] > 0) return i;
//         }
//         return n+1;
//     }
    
    public int firstMissingPositive(int[] nums) {
        cycleSort(nums);
        for(int i=0; i < nums.length; i++){
            if (nums[i] != i+1) return i+1;
        }
        return nums.length+1;
    }
    
    private static void cycleSort(int[] nums){
        int i = 0;
        int n = nums.length;
        while(i < n){
            int j = nums[i]-1;
            if (j>=0 && j < n && nums[i] != nums[j] ) swap(nums, i, j);
            else i++;
        }
    }
    
    private static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}