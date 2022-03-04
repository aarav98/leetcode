class Solution {
    public int minMeetingRooms(int[][] intervals) {
        
        Arrays.sort(intervals, (a,b)-> Integer.compare(a[0], b[0])); // Sort by start time
        int rooms = 0;
        
        PriorityQueue<int[]> concurrentMeetings = new PriorityQueue<>(intervals.length, (a,b)->Integer.compare(a[1],b[1]));
        
        for(int[] interval: intervals){
            while(!concurrentMeetings.isEmpty() && interval[0] >= concurrentMeetings.peek()[1]){
                concurrentMeetings.poll();
            }
            concurrentMeetings.add(interval);
            rooms = Math.max(rooms, concurrentMeetings.size());
                
        }
        return rooms;
        
    }
    
    
}