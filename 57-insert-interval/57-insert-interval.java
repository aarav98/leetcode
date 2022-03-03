class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        LinkedList<int[]> list = new LinkedList<>();
        
        int i;
        for(i = 0;i<intervals.length; i++){
            if(intervals[i][1] < newInterval[0]){
                list.add(intervals[i]);
            }else{
                break;
            }
        }
        
        list.add(newInterval);
        
        for(;i<intervals.length; i++){
            if(list.getLast()[1] >= intervals[i][0] && list.getLast()[0] <= intervals[i][1]){
                list.getLast()[0] = Math.min(list.getLast()[0], intervals[i][0]);
                list.getLast()[1] = Math.max(list.getLast()[1], intervals[i][1]);
            }else{
                list.add(intervals[i]);
            }
        }
        
        
        return list.toArray(new int[list.size()][]);
        
    }
}