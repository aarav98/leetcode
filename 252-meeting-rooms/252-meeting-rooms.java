class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a,b)-> Integer.compare(a[0], b[0]));
        
        int i = 1;
        while(i < intervals.length){
            if(intervals[i-1][1] > intervals[i++][0]) return false;
        }
        return true;
            
    }
}