class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b)->Integer.compare(a[0], b[0]));
        
        Stack<int[]> merged = new Stack<>();
        
        for(int[] interval:intervals){
            if(merged.isEmpty() || merged.peek()[1] < interval[0]) merged.add(interval);
            
            merged.peek()[1] = Math.max(merged.peek()[1], interval[1]);
        }
        
        return merged.toArray(new int[merged.size()][]);
        
    }
}
